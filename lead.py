import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set the display dimensions
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Leaderboard")

# Font settings
font = pygame.font.SysFont(None, 40)
heading_font = pygame.font.SysFont(None, 50)

# Define the file path for the leaderboard file
leaderboard_file = "lead.txt"

def load_leaderboard():
    """Load the leaderboard from a text file."""
    if not os.path.exists(leaderboard_file):
        return {}
    
    leaderboard = {}
    with open(leaderboard_file, 'r') as file:
        for line in file:
            if line.strip():
                player, score = line.strip().split(':')
                leaderboard[player] = int(score)
    return leaderboard

def save_leaderboard(leaderboard):
    """Save the leaderboard to a text file."""
    with open(leaderboard_file, 'w') as file:
        for player, score in leaderboard.items():
            file.write(f"{player}:{score}\n")

def display_leaderboard(leaderboard):
    # Initialize Pygame
    #pygame.init()

    # Set the display dimensions
    window_width = 600
    window_height = 400
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Leaderboard")

    """Display the leaderboard in a new Pygame window in a table format."""
    window.fill((0, 0, 0))  # Fill window with black background
    
    # Sort the leaderboard by scores in descending order
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
    
    # Render the "LEADERBOARD" heading at the top
    heading_surface = heading_font.render("LEADERBOARD", True, (255, 215, 0))  # Gold text color
    window.blit(heading_surface, (window_width // 2 - heading_surface.get_width() // 2, 20))

    # Render each player's score in a table format
    y_offset = 100
    window.blit(font.render("Rank", True, (255, 255, 255)), (50, y_offset - 40))
    window.blit(font.render("Player", True, (255, 255, 255)), (200, y_offset - 40))
    window.blit(font.render("Score", True, (255, 255, 255)), (450, y_offset - 40))

    for index, (player, score) in enumerate(sorted_leaderboard):
        rank_text = font.render(str(index + 1), True, (255, 255, 255))
        player_text = font.render(player, True, (255, 255, 255))
        score_text = font.render(str(score), True, (255, 255, 255))

        # Display rank, player name, and score in a row (acting as a table row)
        window.blit(rank_text, (50, y_offset))
        window.blit(player_text, (200, y_offset))
        window.blit(score_text, (450, y_offset))

        y_offset += 50  # Move down for the next row

    pygame.display.update()

def add_player_score(username, score):
    """Add a new player and their score to the leaderboard and save the updated leaderboard."""
    leaderboard = load_leaderboard()  # Load current leaderboard
    leaderboard[username] = score     # Add or update the player's score
    save_leaderboard(leaderboard)     # Save the updated leaderboard to the file
    display_leaderboard(leaderboard)  # Display leaderboard when a new score is added

def main():
    # Load the initial leaderboard from the file
    leaderboard = load_leaderboard()
    display_leaderboard(leaderboard)  # Display leaderboard at startup
    
    # Example of how to update the leaderboard dynamically
    add_player_score("NewPlayer", 90)  # Adding a new player with a score

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.delay(100)  # Slow down the loop for demonstration purposes

if __name__ == "__main__":
    main()
