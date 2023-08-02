import pygame
from sys import exit
import math
import os
from random import randint

#* Rocket Class
class Rocket(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		rocket_fly_1 = pygame.image.load('graphics/rocket/rocket_1.png').convert_alpha()
		rocket_fly_2 = pygame.image.load('graphics/rocket/rocket_2.png').convert_alpha()
		rocket_fly_1 = pygame.transform.scale(rocket_fly_1, (100,70))
		rocket_fly_2 = pygame.transform.scale(rocket_fly_2, (100,70))
	 
		self.rocket_fly = [rocket_fly_1, rocket_fly_2]
		self.rocket_index = 0

		self.image = self.rocket_fly[self.rocket_index]
		self.rect = self.image.get_rect(center = (100,320))

		self.is_alive = True

	def player_input(self):
		speed = 20
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] and self.rect.top > 20: self.rect.top -= speed
		if keys[pygame.K_DOWN] and self.rect.bottom < 780: self.rect.bottom += speed
		if keys[pygame.K_RIGHT] and self.rect.right < 1380: self.rect.right += speed
		if keys[pygame.K_LEFT] and self.rect.left > 20: self.rect.left -= speed
			
	def animation_state(self):
			self.rocket_index += 0.1
			if self.rocket_index >= len(self.rocket_fly):self.rocket_index = 0
			self.image = self.rocket_fly[int(self.rocket_index )] 
    
	def update(self):
		self.player_input()
		self.animation_state()
		
#* Asteroid Class
class Asteroid(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		
		asteroid = pygame.image.load("graphics/asteroid/asteroidsprite.png").convert_alpha()
		asteroid = pygame.transform.scale(asteroid, (120,90)) 
		self.image = asteroid
		self.rect = self.image.get_rect(center = (1500, randint(0,800)))
	
	def destroy(self):
		if self.rect.x <= -100:
			self.kill()			

	def update(self):
		self.destroy()
		self.movement()
		
	def movement(self):
		self.rect.x -= 15
		
#* Score Display
def display_score(start_time, screen, test_font):
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (700,50))
	screen.blit(score_surf,score_rect)
	return current_time
	
#* Collision Detection
def collision_sprite(rocket, asteroid_group):
	if pygame.sprite.groupcollide(rocket, asteroid_group,False, True):
		asteroid_group.empty()
		return False
	else: return True

#* Function to update high score
def update_high_score(score):
    
    #* Check if txt file exists
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as file:
            file.write("0")

    #* Read the previous high score txt file
    with open("highscore.txt", "r") as file:
        previous_high_score = int(file.read())

    #* Check if the current score is higher than previous  score
    if score > previous_high_score:
        # Update the high score in the file
        with open("highscore.txt", "w") as file:
            file.write(str(score))

    #* Return current high score
    return max(score, previous_high_score)


def main():
	#* Initializing Pygame, Clock, Screen, Font, Score, Game Status and Time
	pygame.init()
	screen = pygame.display.set_mode((1400,800))
	pygame.display.set_caption('Space Evader')
	clock = pygame.time.Clock()
	test_font = pygame.font.Font('graphics/Pixeboy-z8XGD.ttf', 70)
	game_active = False
	start_time = 0
	score = 0

	#* Music
	background_music = pygame.mixer.Sound("audio/music1.mp3")
	background_music.set_volume(0.2)
	background_music.play(loops = -1)


	#* Sprite Groups
	rocket = pygame.sprite.GroupSingle()
	rocket.add(Rocket())
	asteroid_group = pygame.sprite.Group()

	#* Setting up background surface, tiles and initiatlizing scroll for background movement
	space_surface = pygame.image.load('graphics/space1.png').convert()
	scroll = 0
	tiles = math.ceil(1640 / space_surface.get_width()) + 1

	#* Intro Screen
	still_rocket = pygame.image.load('graphics/rocket/rocket_2.png').convert_alpha()
	still_rocket = pygame.transform.scale(still_rocket,(220,190))
	still_rocket_rect = still_rocket.get_rect(center = (700,400))
	game_name = test_font.render('Space Evader',False,(226,226,226))
	game_name_rect = game_name.get_rect(center = (700,150))
	game_message = test_font.render('Press space to start',False,(226,226,226))
	game_message_rect = game_message.get_rect(center = (700,600))

	#* Timer 
	obstacle_timer = pygame.USEREVENT + 1
	pygame.time.set_timer(obstacle_timer,200)

	#* Game Loop
	while True:
		
		#* Quit game option
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if game_active:
				if event.type == obstacle_timer:
					asteroid_group.add(Asteroid())		
			
			#* Start game when spacebar is pressed
			else:
				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					game_active = True
					
					#* Start time
					start_time = int(pygame.time.get_ticks() / 1000)
		
		#* Game has started
		if game_active:
			
			#* Make background move infinitely 
			screen.blit(space_surface,(0,0))
			i = 0
			while i < tiles:
				screen.blit(space_surface, (space_surface.get_width()*i + scroll, 0))
				i+=1
			scroll -= 6
			if abs(scroll) > space_surface.get_width(): scroll = 0
			
			#* Score displayed on screen when playing
			score = display_score(start_time, screen, test_font)
			
			#* Creating a rocket that does its thing
			rocket.draw(screen)
			rocket.update()
			asteroid_group.update()
			asteroid_group.draw(screen)

			game_active = collision_sprite(rocket, asteroid_group)
		
		#* Game Over Screen
		else:
			
			screen.fill((0,0,0))
			screen.blit(still_rocket,still_rocket_rect)
			screen.blit(game_name,game_name_rect)

			#* Display score and high score	
			score_message = test_font.render(f'Your score: {score}',False,(226,226,226))
			score_message_rect = score_message.get_rect(center = (700,600))
			high_score = update_high_score(score)
			high_score_message = test_font.render(f'High Score: {high_score}', False, (226, 226, 226))
			high_score_message_rect = high_score_message.get_rect(center=(700, 700))
			screen.blit(high_score_message, high_score_message_rect)
			if score == 0: screen.blit(game_message,game_message_rect)
			else: screen.blit(score_message,score_message_rect) 

		pygame.display.update()
		clock.tick(60)
	
if __name__=="__main__":
	main()