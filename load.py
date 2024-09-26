import pygame
import time


def show_pygame_loading_screen(total=300, loading_message="Loading...", load_char_color=(0,138,216), bg_color=(0, 0, 0), text_color=(255, 255, 255), complete_message="Almost There!", delay=0.5):
    """Displays a loading screen using Pygame with a progress bar.
    
    Args:
        total (int): Total progress steps (default 300).
        loading_message (str): Message displayed while loading (default "Loading...").
        load_char_color (tuple): RGB color for the loading bar (default green).
        bg_color (tuple): RGB background color (default white).
        text_color (tuple): RGB color for the text (default black).
        complete_message (str): Message displayed when loading is complete (default "Complete!").
        delay (float): Time in seconds between progress updates (default 0.1).
    """
    pygame.init()
    screen = pygame.display.set_mode((600, 150))  # Create a Pygame window
    pygame.display.set_caption('Loading Screen')
    font = pygame.font.SysFont(None, 40)
    
    def draw_text(message, y_pos):
        """Helper function to draw text on the screen."""
        text = font.render(message, True, text_color)
        text_rect = text.get_rect(center=(screen.get_width() // 2, y_pos))
        screen.blit(text, text_rect)
    
    for current_progress in range(total + 1):
        progress_percent = int((current_progress / total) * 100)

        # Fill the screen background
        screen.fill(bg_color)

        # Draw the loading message at the top
        draw_text(loading_message, 50)

        # Draw the progress bar
        bar_width = int((progress_percent / 100) * 500)
        pygame.draw.rect(screen, load_char_color, pygame.Rect(50, 90, bar_width, 20), border_radius=5)


        # Display the percentage completion
        percent_text = f"{progress_percent}%"
        draw_text(percent_text, 130)

        pygame.display.flip()  # Update the display

        # Check for Pygame events (close window, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        time.sleep(delay)  # Simulate a task with a time delay

    # Show the complete message once the loading is done
    screen.fill(bg_color)
    draw_text(complete_message, 90)
    pygame.display.flip()

    time.sleep(2)  # Wait before closing the loading screen

    pygame.quit()


# Test the loading screen function (this would be removed when integrating)
if __name__ == "__main__":
    show_pygame_loading_screen(total=300, delay=0.5)  # Executes for approximately 30 seconds
