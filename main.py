import threading
from gui import create_gui
from schedule_tweet import schedule_tweets

if __name__ == "__main__":
    gui_thread = threading.Thread(target=create_gui)
    schedule_thread = threading.Thread(target=schedule_tweets)

    gui_thread.start()
    schedule_thread.start()

    gui_thread.join()
    schedule_thread.join()
