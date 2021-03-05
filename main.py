import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700, 800))
running = True
score = 0
radius = 20

#colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#snake
x_list = [90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610]
y_list = [140, 180, 220, 260, 300, 340, 380, 420, 460, 500, 540, 580, 620, 660]
x = x_list[random.randint(1, 3)]
y = y_list[random.randint(4, 8)]
speed = 5
snake_x, snake_y = [], []
directions = []

snake_x.append(x)
snake_y.append(y)
directions.append("Right")
turn_x = [""]
turn_y = [""]
snakes = [""]

#power up
pow_x = x_list[random.randint(0, 13)]
pow_y = y_list[random.randint(0, 13)]

#game over
def game_over():
	global speed, black, score, running
	speed = 0
	while running:
		screen.fill(black)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		font = pygame.font.Font('freesansbold.ttf', 70)
		text = font.render(f"Game Over", True, (255, 0, 0), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (350, 400)
		screen.blit(text, textRect)
		
		text = font.render(f"Score: {score}", True, (255, 0, 0), (0, 0, 0))
		textRect = text.get_rect()
		textRect.center = (350, 470)
		screen.blit(text, textRect)
		pygame.display.flip()


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				directions[0] = "Right"
				turn_x[0] = snake_x[0]
				turn_y[0] = snake_y[0]
				
			elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
				directions[0] = "Left"
				turn_x[0] = snake_x[0]
				turn_y[0] = snake_y[0]
				
			elif event.key == pygame.K_UP or event.key == pygame.K_w:
				directions[0] = "Up"
				turn_x[0] = snake_x[0]
				turn_y[0] = snake_y[0]
				
			elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
				directions[0] = "Down"
				turn_x[0] = snake_x[0]
				turn_y[0] = snake_y[0]

	#score
	font = pygame.font.Font('freesansbold.ttf', 30)
	text = font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
	textRect = text.get_rect()
	textRect.center = (70, 40)
	screen.blit(text, textRect)
	
	#frame
	pygame.draw.rect(screen, white, (50, 100, 600, 600))
	pygame.draw.rect(screen, black, (70, 120, 560, 560))
	
	#power up
	power_up = pygame.draw.rect(screen, black, (pow_x-radius, pow_y-radius, radius*2, radius*2))
	pygame.draw.circle(screen, blue, (pow_x, pow_y), radius)
	
	#snake
	for i in range(score+1):
		snakes[i] = pygame.draw.rect(screen, black, (snake_x[i]-radius, snake_y[i]-radius, radius*2, radius*2))
		pygame.draw.circle(screen, red, (snake_x[i], snake_y[i]), radius)
		
		if i != 0:
			turn_x[i] = turn_x[0]
			turn_y[i] = turn_y[0]
			if (snake_x[0] >= snake_x[i]-radius and snake_x[0] <= snake_x[i]+radius) and (snake_y[0] >= snake_y[i]-radius and snake_y[0] <= snake_y[i]+radius):
				game_over()
			if snake_x[i] == turn_x[i] and snake_y[i] == turn_y[i]:
				directions[i] = directions[0]
		
		if directions[i] == "Right":
			snake_x[i] += speed
		elif directions[i] == "Left":
			snake_x[i] -= speed
		elif directions[i] == "Up":
			snake_y[i] -= speed
		elif directions[i] == "Down":
			snake_y[i] += speed

		if snake_x[i] >= 610:
			snake_x[i] = 90
		elif snake_x[i] <= 90:
			snake_x[i] = 610
		elif snake_y[i] >= 660:
			snake_y[i] = 140
		elif snake_y[i] <= 140:
			snake_y[i] = 660
			
	#check collision
	if snakes[0].colliderect(power_up) == True:
		snakes.append("")
		turn_x.append("")
		turn_y.append("")
		score += 1
		if directions[-1] == "Right":
			snake_x.append(snake_x[-1]-radius*2)
			snake_y.append(snake_y[-1])
		elif directions[-1] == "Left":
			snake_x.append(snake_x[-1]+radius*2)
			snake_y.append(snake_y[-1])
		elif directions[-1] == "Up":
			snake_x.append(snake_x[-1])
			snake_y.append(snake_y[-1]+radius*2)
		elif directions[-1] == "Down":
			snake_x.append(snake_x[-1])
			snake_y.append(snake_y[-1]-radius*2)
		directions.append(directions[-1])
		pow_x = x_list[random.randint(0, 13)]
		pow_y = y_list[random.randint(0, 13)]
		
	pygame.display.flip()

pygame.quit()
