import pygame
from sys import exit
import random
import os
import sys


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.paddle_list = [pygame.image.load(self.resource_path(f"files/paddle/paddle_{n}.png")
                                              ).convert_alpha() for n in range(1, 7)]
        self.index = 0
        self.image = self.paddle_list[self.index]
        self.rect = self.image.get_rect(midbottom=(450, 590))

    def controller(self):
        keyboard_keys = pygame.key.get_pressed()
        if keyboard_keys[pygame.K_RIGHT] and self.rect.right <= 895:
            self.rect.right += 10
        if keyboard_keys[pygame.K_LEFT] and self.rect.left >= 7:
            self.rect.left -= 10

    def animate(self):
        self.index += 0.1
        if self.index > len(self.paddle_list):
            self.index = 0
        self.image = self.paddle_list[int(self.index)]

    def update(self):
        self.controller()
        self.animate()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 7
        self.direction = pygame.math.Vector2((random.randint(200, 600), random.randint(200, 600))).normalize()
        self.pos = pygame.math.Vector2(450, 500)
        self.image = pygame.image.load(self.resource_path("files/ball/ball.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(self.pos.x, self.pos.y))

    def reflect(self, nv):
        self.direction = self.direction.reflect(pygame.math.Vector2(nv))

    def movement(self):
        if self.rect.left <= 0:
            self.reflect((1, 0))
            bounce_music.play()
        if self.rect.right >= 900:
            self.reflect((-1, 0))
            bounce_music.play()
        if self.rect.top <= 0:
            self.rect.y += 4
            self.reflect((0, 1))
            bounce_music.play()

    def update(self):
        self.pos -= self.direction * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.movement()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


class Tiles(pygame.sprite.Sprite):
    def __init__(self, position, shape):
        super().__init__()
        self.shape = shape
        self.tiles_list = self.get_tiles(self.shape)
        random.shuffle(self.tiles_list)

        self.image = pygame.image.load(self.resource_path(f"files/tiles_{self.shape}/{self.tiles_list[0]}"))
        self.rect = self.image.get_rect(midleft=position)

    def get_tiles(self, shape):
        tiles_list = []
        for root, dirs, files in os.walk(rf'files/tiles_{shape}'):
            for file in files:
                if file.endswith('.png'):
                    tiles_list.append(file)
        return tiles_list

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(self.resource_path("files/asset/bullet.png")).convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)

    def control(self):
        if self.rect.y > 500:
            self.rect.left = paddle.rect.left

    def update(self):
        self.rect.y -= 5
        self.destroy()

    def destroy(self):
        if self.rect.y <= -100:
            self.kill()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


class Live(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        paddle_center = paddle.rect.centerx
        if paddle_center < 500:
            start_x = paddle.rect.centerx + random.randint(150, 400)
        else:
            start_x = paddle.rect.centerx - random.randint(150, 500)
        self.image = pygame.image.load(self.resource_path("files/asset/live.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(start_x, 600))

    def movement(self):
        self.rect.y -= 2
        if self.rect.top <= 0:
            self.kill()

    def update(self):
        self.movement()

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def ball_collision_with_paddle():
    global ball, paddle_group
    paddle_hit = pygame.sprite.spritecollide(ball, paddle_group, False)
    if paddle_hit:
        ball.reflect((0, -1))
        ball.rect.y += 5
        bounce_music.play()


def ball_collision_with_tiles():
    global tile_group, ball
    tile_hit = pygame.sprite.spritecollide(ball, tile_group, False)
    if tile_hit:
        ball.velocity += 0.2
        bl = tile_hit[0].rect.left - ball.rect.width / 4
        br = tile_hit[0].rect.right + ball.rect.width / 4
        nv = (0, 1) if bl < ball.rect.centerx < br else (1, 0)
        ball.reflect(nv)
        tile_group.remove(tile_hit)
        hit_tile_music.play()


def bullet_collision_with_tiles():
    global bullet_group, tile_group, tile_shot, all_tiles, tile_shot2
    for bull in bullet_group:
        tile_hit = pygame.sprite.spritecollide(bull, tile_group, False)

        if tile_hit:
            bull.kill()
            for tile in tile_hit:
                if tile.rect.width < 100:
                    tile_group.remove(tile_hit)
                else:
                    try:
                        hit_index = all_tiles.index(tile)
                        tile_group.remove(tile_hit)
                        tile_group.add(all_tiles_shot[hit_index])
                    except ValueError:
                        pass


def bullet_collision_with_live():
    global bullet_group, live_group, num_live
    for bull in bullet_group:
        live_hit = pygame.sprite.spritecollide(bull, live_group, False)
        if live_hit:
            bull.kill()
            live_music.play()
            live_group.remove(live_hit)
            if num_live < 5:
                num_live += 1

    image_live = pygame.image.load(resource_path("files/asset/live.png")).convert_alpha()
    image_live_rect = [image_live.get_rect(midbottom=(878 - n, 600)) for n in range(0, 130, 25)]
    for live_rect in image_live_rect[:num_live]:
        window.blit(image_live, live_rect)


def win_or_lose():
    global game_over, continue_game, play, win, num_live, all_tiles, all_tiles_shot
    # Detect ball out and game over
    if ball.rect.bottom >= 620:
        play = False
        if num_live < 2:
            game_over = True
            tile_group.empty()
            all_tiles = tile1 + tile2
            tile_group.add(all_tiles)
            ball.velocity = 7
            return "GAME OVER: LIVE LESS THAN 2"
        else:
            continue_game = True
            return f"PLAY ON: CONTINUE WITH 2 LIVES"

    # Detect player win
    if not tile_group and ball.rect.y > random.randint(100, 300):
        win = True
        play = False
        all_tiles_shot = tile_shot + tile4 + tile_shot2
        all_tiles = tile1 + tile2 + tile3 + tile4
        tile_group.add(all_tiles)
        ball.velocity = 7
        return "YOU WIN!"


def menu_window():
    global game_over_rect, game_over_text, num_live, text
    window.fill("#30475E")

    if num_live == 1:
        x_pos = 450
    elif num_live == 2:
        x_pos = 470
    elif num_live == 3:
        x_pos = 490
    elif num_live == 4:
        x_pos = 502
    else:
        x_pos = 530

    image_live = pygame.image.load(resource_path("files/asset/live.png")).convert_alpha()
    image_live_rect = [image_live.get_rect(center=(x_pos - n, 80)) for n in range(0, 220, 40)]
    for live_rect in image_live_rect[:num_live]:
        window.blit(image_live, live_rect)

    game_over_text = font.render(text, False, "#F5F5F5")
    game_over_rect = game_over_text.get_rect(center=(450, 140))
    window.blit(game_over_text, game_over_rect)

    logo = pygame.image.load(resource_path("files/asset/screen logo.png")).convert_alpha()
    logo_rect = logo.get_rect(center=(450, 280))
    window.blit(logo, logo_rect)

    instruction_text = font.render("Press enter to play!", False, "#F05454")
    instruction_rect = instruction_text.get_rect(center=(450, 400))
    window.blit(instruction_text, instruction_rect)


def opening_window():
    global game_stated
    game_time = pygame.time.get_ticks() // 1000
    font1 = pygame.font.Font(resource_path("files/font/ken_vector_future_thin.ttf"), 60)
    font2 = pygame.font.Font(None, 30)
    if game_time < 5:
        menu_music.set_volume(0.5)
        window.fill("#30475E")

        welcome_text = font1.render("WELCOME TO", False, "#F5F5F5")
        welcome_text_rect = game_over_text.get_rect(center=(365, 140))
        window.blit(welcome_text, welcome_text_rect)

        logo = pygame.image.load(resource_path("files/asset/screen logo.png")).convert_alpha()
        logo_rect = logo.get_rect(center=(450, 280))
        window.blit(logo, logo_rect)

        instruction_text = font2.render("Press LEFT or RIGHT to move the Paddle", False, "#F05454")
        instruction_rect = instruction_text.get_rect(center=(450, 400))
        window.blit(instruction_text, instruction_rect)
    else:
        game_stated = True
        menu_music.set_volume(0)
        bg_music.set_volume(1)
        gunshot_music.set_volume(0.3)


def create_tiles_list(x, y, n, k, shape):
    tile_list = [Tiles(shape=shape, position=(5 + x * i, y + k * j))
                 for i in range(n) for j in range(2)]
    return tile_list


# WINDOW
pygame.init()
window = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Break-Out-2")
icon = pygame.image.load(resource_path("files/asset/logo.ico")).convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
num_live = 3

# TEXT
text = "BREAK-OUT-II"
font = pygame.font.Font(resource_path("files/font/ken_vector_future_thin.ttf"), 30)
game_over_text = font.render(text, False, "#F5F5F5")

# PADDLE
paddle_group = pygame.sprite.Group()
paddle = Paddle()
paddle_group.add(paddle)

# BALL
ball_group = pygame.sprite.Group()
ball = Ball()
ball_group.add(ball)

# TILES
tile_group = pygame.sprite.Group()
tile1 = create_tiles_list(x=112, y=20, n=8, k=44, shape="rect")
tile_shot = create_tiles_list(x=112, y=20, n=8, k=44, shape="rect_b")

tile2 = create_tiles_list(x=56, y=115, n=16, k=54, shape="sqr")

tile3 = create_tiles_list(x=112, y=218, n=8, k=44, shape="rect")
tile_shot2 = create_tiles_list(x=112, y=218, n=8, k=44, shape="rect_b")

tile4 = create_tiles_list(x=56, y=310, n=16, k=54, shape="sqr")

all_tiles_shot = tile_shot
all_tiles = tile1 + tile2
tile_group.add(all_tiles)

# BULLET
bullet_group = pygame.sprite.Group()

# LIVE
live_group = pygame.sprite.Group()
live = Live()
live_group.add(live)

# MUSIC
bg_music = pygame.mixer.Sound(resource_path("files/music/fat_shadow_-_epic_kill.mp3"))
bg_music.play(loops=-1)
bg_music.set_volume(0)

gunshot_music = pygame.mixer.Sound(resource_path("files/music/gun_shot.wav"))
gunshot_music.play(loops=-1)
gunshot_music.set_volume(0)

menu_music = pygame.mixer.Sound(resource_path("files/music/menu.mp3"))
menu_music.play(loops=-1)

live_music = pygame.mixer.Sound(resource_path("files/music/live.mp3"))
hit_tile_music = pygame.mixer.Sound(resource_path("files/music/breaking tile.mp3"))
bounce_music = pygame.mixer.Sound(resource_path("files/music/bounce-ball.mp3"))


# GAME MANUAL EVENTS
display_menu = pygame.USEREVENT + 1
pygame.time.set_timer(display_menu, 3000)

shoot_bullet = pygame.USEREVENT + 2
pygame.time.set_timer(shoot_bullet, 500)

add_live = pygame.USEREVENT + 3
pygame.time.set_timer(add_live, 3000)

fps = 60
start_time = 0
game_stated, play, win, game_over, continue_game = False, True, False, False, False
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_stated and play and event.type == shoot_bullet:
            bullet = [Bullet(position=(paddle.rect.left + n, 530))
                      for n in range(6, 200, 175)]
            bullet_group.add(bullet)
        if game_stated and play and event.type == add_live:
            live = Live()
            live_group.add(live)
        if game_stated and not play and event.type == display_menu:
            menu_window()

    opening_window()
    if game_stated:
        if play:
            # WINDOW
            window.fill("#121212")
            game_over_rect = game_over_text.get_rect(center=(450, 280))

            # PADDLE
            paddle_group.draw(window)
            paddle_group.update()

            # BULLET
            bullet_group.draw(window)
            bullet_group.update()

            # BALL
            ball_group.draw(window)
            ball_group.update()

            # TILES
            tile_group.draw(window)
            tile_group.update()

            # ADD LIVE
            live_group.draw(window)
            live_group.update()

            # BALL COLLISION WITH TILES
            ball_collision_with_tiles()

            # COLLISION BALL AND PADDLE
            ball_collision_with_paddle()

            # COLLISION TILE WITH BULLET
            bullet_collision_with_tiles()

            # DETECT BULLET COLLISION WITH LIVE
            bullet_collision_with_live()

            # GAME OVER AND WIN LOGIC
            text = win_or_lose()
        else:
            bg_music.set_volume(0)
            gunshot_music.set_volume(0)
            menu_music.set_volume(0.5)
            window.blit(game_over_text, game_over_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                ball.pos = pygame.math.Vector2(450, 500)
                ball.direction = pygame.math.Vector2((random.randint(200, 600), random.randint(200, 600))).normalize()
                paddle.rect.x = 350
                if continue_game:
                    num_live -= 2
                if game_over:
                    num_live = 3
                if win:
                    num_live = num_live
                game_over_text = font.render("BREAK-OUT-II", False, "#F5F5F5")
                play, game_over, win, continue_game = True, False, False, False

    pygame.display.update()
