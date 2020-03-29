import pygame
import time

pygame.init()
pygame.display.set_mode()

score_up = 0 
score_down = 0 

time.sleep(5)

print('go')

for i in range(150):
   
    status_keyboard = pygame.key.get_pressed()
    print(status_keyboard[pygame.K_UP])
    pygame.event.pump()
    time.sleep(0.05)

print("score up : ",score_up)
print("score down :",score_down )

pygame.quit()