import pygame
import cv2

def play_background_video(video_path):
    """ Play a video file and return the video capture object. """
    cap = cv2.VideoCapture(video_path)
    return cap

def display_score(score):
    # Initialize Pygame
    pygame.init()
    
    # Set up the display window (e.g., 1920x960 resolution)
    screen = pygame.display.set_mode((1920, 960))
    
    # Define font for the score
    score_font = pygame.font.Font(None, 100)  # Size for the score

    animation_font = pygame.font.Font(None, 150)
    
    # Define a clock to manage the frame rate
    clock = pygame.time.Clock()
    
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gold = (255, 215, 0)
    
    # Play background video
    video_path = 'congrats.gif'  # Path to your video file
    cap = play_background_video(video_path)

    # Get the start time
    start_time = pygame.time.get_ticks()

    # Main loop to display the scoreboard
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time  # Calculate elapsed time

        # Check if 5 seconds have passed, if so, exit the loop
        if elapsed_time > 3500:
            print("Auto-closing the window after 5 seconds.")
            running = False

        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to the beginning if it ends
            continue

        #Resize the frame to match the window size
        frame = cv2.resize(frame, (960, 1920))

        # Convert the frame to RGB format and create a Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame)

        # Blit the frame onto the screen
        screen.blit(frame_surface, (0, 0))

        # Render the score as text
        score_text = score_font.render(f"Score: {score:.0f}", True, white)
        score_rect = score_text.get_rect(center=(960, 530))  # Center the text
        screen.blit(score_text, score_rect)

        # Add some fun animation text
        animation_text = animation_font.render("Congratulations!", True, gold)
        animation_rect = animation_text.get_rect(center=(960, 430))
        screen.blit(animation_text, animation_rect)

        # Event handling (allow closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update the display
        pygame.display.update()
        
        # Cap the frame rate to 60 FPS
        clock.tick(60)

    # Release the video capture object and quit Pygame
    cap.release()
    pygame.quit()

# Example usage:
if __name__ == "__main__":
    final_score = 85  # This score will come from your score logic
    display_score(final_score)
