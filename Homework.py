import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Matching Game")

font = pygame.font.SysFont("Arial", 36)
white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)

Candy = pygame.image.load("Homework/img/Candy.png")
ludo_img = pygame.image.load("Homework/img/Ludo.png")

screen.fill(black)
screen.blit(Candy, (150, 200))
screen.blit(ludo_img, (150, 400))

text1 = font.render("Ludo", True, white)
text2 = font.render("Candy", True, white)

screen.blit(text1, (350, 400))
screen.blit(text2, (350, 200))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                result = "You chose ALIBABACandy!"
            elif event.key == pygame.K_2:
                result = "You chose SKIBIDILudo!"
            screen.fill(black)
            screen.blit(Candy, (150, 200))
            screen.blit(ludo_img, (150, 400))
            screen.blit(text1, (350, 400))
            screen.blit(text2, (350, 200))
            message = font.render(result, True, red)
            screen.blit(message, (50, 50))
            pygame.display.update()
            
            

pygame.quit()

