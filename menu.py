import pygame
import shooter_game

pygame.init()
window = pygame.display.set_mode((600, 600))



bg = pygame.image.load("galaxy.jpg")
bg = pygame.transform.scale(bg,(600, 600))



time = pygame.time.Clock()


button_rect = pygame.Rect(200, 200, 100, 50)

button_exit = pygame.Rect(200, 270, 100, 50)

running= True 
pygame.font.init()
bed = pygame.font.SysFont("Arial", 35).render("Start", True, (255, 255, 255))
exit_bed = pygame.font.SysFont("Arial", 35).render("Exit", True, (255, 255, 255))
while running:
    window.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if button_rect.collidepoint(event.pos):
                shooter_game.game()
                pygame.quit()






    pygame.draw.rect(window, (100, 123, 213), button_rect)
    pygame.draw.rect(window, (100, 123, 213), button_exit)
    window.blit(bed, (225,  210))
    window.blit(exit_bed, (230,  280))
    pygame.display.update()
    time.tick(50)