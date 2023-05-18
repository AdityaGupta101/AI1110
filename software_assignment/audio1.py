import os
import numpy as np
import tkinter as tk
from tkinter import messagebox
from playsound import playsound

# Specify the directory path where your audio files are located
audio_directory = "/Users/adityagupta/Desktop/Audio1/mov"

# Get a list of all audio files in the directory
audio_files = [file for file in os.listdir(audio_directory) if file.endswith(".MOV")]
np.random.shuffle(audio_files)

current_song_index = 0

def play_song():
    global current_song_index
    if current_song_index < len(audio_files):
        song_path = os.path.join(audio_directory, audio_files[current_song_index])
        playsound(song_path)

def stop_song():
    messagebox.showinfo("Stop", "Song stopped.")

def next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index < len(audio_files):
        song_path = os.path.join(audio_directory, audio_files[current_song_index])
        playsound(song_path)
    else:
        messagebox.showinfo("End of Playlist", "No more songs in the playlist.")

# Create the main application window
window = tk.Tk()

# Create buttons
play_button = tk.Button(window, text="Play", command=play_song)
play_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_song)
stop_button.pack()

next_button = tk.Button(window, text="Next", command=next_song)
next_button.pack()

# Run the main event loop
window.mainloop()
