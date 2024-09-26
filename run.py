import os
import threading

from username import username_input_window
from score import markscore
from lead import add_player_score


username = ""

def run_script(script):
    """Function to run a python script."""
    result = os.system(f"python {script}")
    if result != 0:
        print(f"Error executing {script}")
        exit(1)

if __name__ == "__main__":

    while True:
        username = username_input_window()
        if username != "":
        
            # Run 03_record_dance.py to capture video from the webcam
            print("Running 03_record_dance.py...")
            run_script("03_record_dance.py")
    
            # Create threads to run annotate_vid.py and load.py concurrently
            print("Running annotate_vid.py and load.py concurrently...")

            annotate_thread = threading.Thread(target=run_script, args=("annotate_vid.py",))
            load_thread = threading.Thread(target=run_script, args=("load.py",))

            # Start both threads
            annotate_thread.start()
            load_thread.start()

            # Wait for annotate_vid.py to complete but keep load.py running
            annotate_thread.join()
            load_thread.join()

            # After annotate_vid.py is done, run score.py while load.py continues
            print("Running score.py and load2.py while load2.py...")
            score_thread = threading.Thread(target=run_script, args=("score.py",))
            load2_thread = threading.Thread(target=run_script, args=("load2.py",))

            #mark = markscore()

            #print('username', username)
            #print('score', mark)

            # Start the score.py thread
            score_thread.start()
            load2_thread.start()

            # Wait for score.py and load.py to complete
            score_thread.join()
            load2_thread.join()

            print("Running leaderboard...")
            run_script("lead.py")

            print("All scripts executed successfully!")
            username = ""
