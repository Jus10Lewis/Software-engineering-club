import pygame
from random import randint

alien_delay = 0
last_alien_created_time = 0
def set_next_alien_delay(self):
    """Set the delay time to a random int between 0.5 - 2 seconds"""
    global alien_delay
    alien_delay = randint(500, 2000)

def time_to_create_another_alien(self):
    """Returns True if it's time to create an alien"""
    global last_alien_created_time
    now = pygame.time.get_ticks()
    if now - last_alien_created_time >= alien_delay:
        last_alien_created_time = now
        set_next_alien_delay(self)
        return True
    else:
        return False