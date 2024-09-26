import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the display dimensions
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Enter Username")

# Font settings
font = pygame.font.SysFont(None, 40)
heading_font = pygame.font.SysFont(None, 50)

def username_input_window():
    """Create a window to input the username."""
    input_active = True
    username = ""
    input_box = pygame.Rect(200, 150, 400, 50)  # Input box position and size
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    txt_surface = font.render(username, True, color)

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press Enter to confirm input
                    print(f"Entered Username: {username}")  # Print the username to the console
                    input_active = False  # Close the input window
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode  # Add the typed character

        # Redraw input box and text
        window.fill((0, 0, 0))  # Clear the window
        txt_surface = font.render(username, True, color)
        width = max(200, txt_surface.get_width() + 10)  # Adjust input box width
        input_box.w = width

        # Draw the input box
        pygame.draw.rect(window, color, input_box, 2)  # Draw outline
        window.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw text

        # Render heading
        heading_surface = heading_font.render("Enter Username:", True, (255, 215, 0))
        window.blit(heading_surface, (window_width // 2 - heading_surface.get_width() // 2, 50))

        pygame.display.flip()
    pygame.quit()  # Quit Pygame
    if username == "":
        sys.exit()

    with open("lead.txt", "a") as file:  # Open file in append mode
            file.write(f"{username}:")  # Write username and score as a comma-separated line
    return username


if __name__ == "__main__":
    username_input_window()
