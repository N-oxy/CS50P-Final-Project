#### Video Demo:  <https://www.youtube.com/watch?v=Xw56r7BAuGI>

## Description:
This project is a pixel-game in which the user controls a rocket that must evade asteroids.
The objective is to survive as long as possible and achieve the highest score. The game features a scrolling space background, a rocket that can be moved in four directions, and randomly generated asteroids.

## Project Structure:
    - project.py
    - test_project.py
    - requirements.txt
    - README.MD
    - audio
    - graphics

## Libraries:
**Pygame**: This library is for creating 2D games in Python. It provides various functionalities for game development, including handling graphics, sound, input events, etc. To install Pygame, you can use the following command: **pip install pygame**

## How to Play:
1/ Install Python and Pygame on your computer (if not already installed).
2/ Clone this repository to your local machine or download the ZIP file.
3/ Run the project.py file to start the game.
4/ Use the arrow keys to control the rocket.
5/ Avoid colliding with the incoming asteroids.
6/ Try to survive as long as possible and achieve the highest score.

## Classes:
### Rocket Class:
The Rocket class represents the player-controlled rocket in the game. 

- **player_input(self)**: Handles player input by reading the arrow keys and moving the rocket accordingly.

- **animation_state(self)**: Updates the rocket's animation state to make it look like it's flying.

- **update(self)**: Updates the rocket's position and animation state in each game loop iteration.

### Asteroid Class:
The Asteroid class represents the asteroids that the player needs to avoid.

- **destroy(self)**: Checks if the asteroid has moved off the screen and deletes it if it has.

- **update(self)**: Updates the asteroid's position and checks for destruction in each game loop iteration.

- **movement(self)**: Moves the asteroids from the right side of the screen to the left side.


## Functions:
### Display_score():
This function calculates and displays the player's score on the game screen. It takes three parameters:
- **start_time**: The time when the game started (in seconds).
- **screen**: The game window surface where the score will be displayed.
- **test_font**: The font used for rendering the score text.

### Collision_sprite():
This function handles the collision detection between the rocket and the asteroids. It takes two parameters:
- **rocket**: The rocket sprite object.
- **asteroid_group**: A group containing all the asteroids in the game.

It uses **pygame.sprite.groupcollide()** to check if there is any collision between the rocket and the asteroids. If a collision is detected, the game ends.

### Update_high_score():
This function updates and stores the high score achieved in the game. The high score is saved in a file named **highscore.txt**.
