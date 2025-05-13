import pygame
import sys
from game_controller import GameController
from sound_player import SoundPlayer
from timer import Timer

def main():
    pygame.init()
    
    # Set up the game window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My Game")
    
    # Initialize game components
    game_controller = GameController()
    sound_player = SoundPlayer()
    timer = Timer()
    
    # Load background music
    sound_player.play_background_music()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Update game state
        game_controller.update()
        
        # Render game
        screen.fill((0, 0, 0))  # Clear screen with black
        game_controller.render(screen)
        
        pygame.display.flip()  # Update the display

        # Control the frame rate
        timer.tick(60)

if __name__ == "__main__":
    main()