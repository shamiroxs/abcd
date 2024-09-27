import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set the display dimensions
window_width = 1100
window_height = 960
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Leaderboard")

# Font settings
font = pygame.font.SysFont(None, 80)
heading_font = pygame.font.SysFont(None, 100)

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
    """Display the leaderboard in a new Pygame window in a table format."""
    window.fill((0, 0, 0))  # Fill window with black background
    
    # Sort the leaderboard by scores in descending order
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)
    
    # Render the "LEADERBOARD" heading at the top
    heading_surface = heading_font.render("LEADERBOARD", True, (255, 215, 0))  # Gold text color
    window.blit(heading_surface, (window_width // 2 - heading_surface.get_width() // 2, 20))

    # Render each player's score in a table format
    y_offset = 140
    window.blit(font.render("Rank", True, (255, 255, 255)), (50, y_offset - 40))
    window.blit(font.render("Player", True, (255, 255, 255)), (300, y_offset - 40))
    window.blit(font.render("Score", True, (255, 255, 255)), (900, y_offset - 40))

    # Change the font to one that supports emojis, like Segoe UI Emoji (Windows)
    emoji_font = pygame.font.SysFont('Segoe UI Emoji', 40)  # or 'Apple Color Emoji' on macOS

    for index, (player, score) in enumerate(sorted_leaderboard):
        rank_text = font.render(str(index + 1), True, (255, 255, 255))
        player_text = font.render(player, True, (255, 255, 255))
        score_text = font.render(str(score), True, (255, 255, 255))

        # Display medals for the top 5 players
        if index == 0:
            rank_text = emoji_font.render("🥇", True, (255, 255, 255))  # Gold for 1st place
        elif index == 1:
            rank_text = emoji_font.render("🥈", True, (255, 255, 255))  # Silver for 2nd place
        elif index == 2:
            rank_text = emoji_font.render("🥉", True, (255, 255, 255))  # Bronze for 3rd place
        elif index == 3 or index == 4:
            rank_text = emoji_font.render("🏅", True, (255, 255, 255))  # Medals for 4th and 5th places
            

        # Display rank, player name, and score in a row (acting as a table row)
        window.blit(rank_text, (50, y_offset + 40))
        window.blit(player_text, (300, y_offset + 40))
        window.blit(score_text, (900, y_offset + 40))

        y_offset += 80  # Move down for the next row

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

    # Get the start time
    start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time

        # Automatically close the window after 5 seconds
        if elapsed_time > 8000:
            print("Auto-closing the leaderboard window after 5 seconds.")
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.delay(100)  # Slow down the loop for demonstration purposes

if __name__ == "__main__":
    main()
