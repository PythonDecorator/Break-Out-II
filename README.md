# [Break-Out-II: A Modern Breakout Game using Pygame](https://github.com/PythonDecorator)
<br />

![version](https://img.shields.io/badge/version-1.0.0-blue.svg)

--- 
![break-out-II-BG](https://github.com/PythonDecorator/Break-Out-II/assets/133740663/1455bb5f-d6ed-4d11-bf35-5b02a5e7ce1f)

## Table of Contents

* [Overview](#overview)
* [Demo](#demo)
* [Documentation](#documentation)
* [Features](#features)
* [Converting to Executable](#converting-to-executable)
* [Controls](#Controls)
* [Licensing](#license)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [For Open Source](#For-open-source)
* [Social Media](#Social-media)

<br />


## Overview

Break-Out-II is an exciting and modern take on the classic Breakout arcade game, developed using the Python programming
language and the Pygame library. This game was built based on the Official Pygame documentation.

The purpose of the project is to capture the essence of the original Breakout game while infusing it with enhanced
graphics, dynamic gameplay, lives, levels and a user-friendly interface.

By building Break-Out-II, I was able to delve into the realm of game development, learning key concepts while creating
an engaging and entertaining gaming experience.

- The game consist of 5 lives in order to clear out all the blocks.
- Try and break all the blocks to win.
- Try and shoot a live, you can only have maximum of 5 lives.
- With each fall, you will need two lives to continue, If all the lives are lost or less than two, then the game is over.



## Demo
- **Download the One file .exe file from the dist or download folder**
- **You don't need to install anything, just download, click and start playing.**


<br />

## Features
> Game main Features

1. ✅ `Intuitive Controls`: Implemented a smooth and responsive controls, allowing players to maneuver the paddle with
   precision using keyboard.

2. ✅ `Vibrant Visuals`: Crafted visually appealing graphics for the paddle, ball, and bricks with animations.

3. ✅ `Diverse Brick Types`: Designed various types of bricks, each with unique properties such as different colors,
   strengths, and point values. Break through them strategically to maximize your score.

4. ✅ `Bullets`: Introduced Bullets that can shoot the square tiles an only crack the rectangular tiles, gets on live
   when the bullet hits a live.

5. ✅ `Dynamic Physics`: Realistic ball physics with proper collision handling, ensuring accurate bounces off walls, the
   paddle, and bricks

6. ✅ `Progressive Levels`: Multiple levels with varying brick arrangements, introducing increasing levels of challenge
   as players advance through the game.

7. ✅ `Sound Effects and Music`: Enhanced gaming experience with sound effects for ball interactions, brick destruction,
   and background music that complements the game's atmosphere.

8. ✅ `User Interface`: Design an engaging user interface with start and pause menus, level indicators, and a game over
   screen displaying the final score.

9. ✅ `Lives`: Implemented lives logic where players use 2 lives to restart the game. The lives are gotten by shooting a
   lives in the game.


## Documentation
This game was built based on the Pygame documentation

## Converting to Executable

PyInstaller is a popular tool that allows you to convert Python scripts into standalone executable files for various
platforms, effectively creating desktop applications.

- You can use PyInstaller options to customize the behavior and appearance of the generated executable. Refer to the
PyInstaller documentation for more information on available options.
- Keep in mind that PyInstaller generates a self-contained executable, but the size of the executable might be larger due
to the inclusion of the Python interpreter and any dependencies, it's best to use venv to make sure only packages used in the
project are included.
- Be sure to test the generated executable on the
target platform to ensure everything works as expected.

<br />

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Create the .exe file

```bash
$ pyinstaller main.spec 
```

<br />

  
## Controls

Press the left or right key to control the paddle.

## License

This project is licensed under the MIT license. See also the attached LICENSE file.

## Reporting Issues

GitHub Issues is the official bug tracker for the Break-Out-II.

## Technical Support or Questions

If you have questions contact me okpeamos.ao@gmail.com instead of opening an issue.


Make sure that you are using the latest version of the Break-Out-II. Check the CHANGELOG
Provide reproducible steps for the issue will shorten the time it takes for it to be fixed.

## For Open Source

The "Break-Out-II" project offers an exciting journey into the world of game development,
enabling you to create a captivating and modern version of the classic Breakout game. Through this project, you'll not
only refine your Python programming skills but also gain valuable insights into game design principles and interactive
user experiences. Whether you're a novice seeking an introduction to game development or an experienced programmer
looking to expand your skillset, Break-Out-II provides a hands-on opportunity to create an engaging game that you can
proudly share with others.


## Social Media

- Twitter: <https://twitter.com/AmosBrymo67154>
- Instagram: <https://www.instagram.com/pythondecorator>

<br />

---

