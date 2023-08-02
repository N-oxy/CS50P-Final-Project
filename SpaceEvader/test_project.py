import pygame
import os
from project import display_score, collision_sprite, update_high_score, Rocket, Asteroid

def test_display_score():
    start_time = 0
    screen = pygame.Surface((1400, 800))
    test_font = pygame.font.Font('graphics/Amatic-Bold.ttf', 70)
    current_time = display_score(start_time, screen, test_font)
    assert current_time == 0

def test_update_high_score():
    with open("highscore.txt", "w") as file:
        file.write("100")
    score = 200
    updated_high_score = update_high_score(score)
    assert updated_high_score == score
    os.remove("highscore.txt")

def test_collision_sprite():
    rocket = Rocket()
    asteroid_group = pygame.sprite.Group()
    asteroid_group.add(Asteroid())
    collision_result = collision_sprite(rocket, asteroid_group)
    assert isinstance(collision_result, bool)

