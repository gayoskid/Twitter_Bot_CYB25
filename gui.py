import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from twitter_api import post_tweet

def browse_image():
    file_path = filedialog.askopenfilename()
    # Process the selected image file

def post_tweet_gui(text):
    post_tweet(text)  # Call the post_tweet function from twitter_api.py to post the tweet immediately
    print("Tweet posted:", text)

def create_gui():
    root = tk.Tk()
    root.title("Twitter Bot")

    # Load and set the background image
    background_image = Image.open("botbg.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Set the size of the text entry field
    text_entry = tk.Text(root, height=20, width=80, font=("Helvetica", 14))
    text_entry.pack(pady=20)  # Add padding to center the text entry field vertically

    # Browse Image button
    browse_button = tk.Button(root, text="Browse Image", command=browse_image, font=("Helvetica", 12))
    browse_button.pack(pady=20)  # Add padding to center the button vertically

    # Post Tweet button
    post_button = tk.Button(root, text="Post_Tweet", command=lambda: post_tweet_gui(text_entry.get("1.0", tk.END)), font=("Helvetica", 12))
    post_button.pack(pady=20)  # Add padding to center the button vertically

    # Center the window on the screen
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()
