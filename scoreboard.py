import pygame

def display_score(score):
    # Initialize Pygame
    pygame.init()
    
    # Set up the display window (e.g., 800x600 resolution)
    screen = pygame.display.set_mode((800, 600))
    
    # Define a font for the scoreboard
    font = pygame.font.Font(None, 74)
    
    # Define a clock to manage the frame rate
    clock = pygame.time.Clock()
    
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Main loop to display the scoreboard
    running = True
    while running:
        screen.fill(black)  # Fill the background with black
        
        # Render the score as text
        score_text = font.render(f"Score: {score:.2f}", True, white)
        screen.blit(score_text, (300, 250))  # Position the text on the screen
        
        # Event handling (allow closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the display
        pygame.display.update()
        
        # Cap the frame rate to 60 FPS
        clock.tick(60)
    
    # Quit Pygame
    pygame.quit()

# Example usage:
if __name__ == "__main__":
    final_score = 85  # This score will come from your `00_score.py` logic
    display_score(final_score)
