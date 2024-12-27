import customtkinter as ctk
import os
import sys
import subprocess

# Setup
if not os.path.isdir(r"userdata\series"):
    os.makedirs(r"userdata\series")

# Global settings
DIR_PATH = r"userdata\series"

# Function to suppress the console window (Windows)
def suppress_console():
    if sys.platform.startswith("win") and "--detached" not in sys.argv:
        subprocess.Popen(
            [sys.executable] + sys.argv + ["--detached"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sys.exit()

# Series management
def load_series():
    return [f for f in os.listdir(DIR_PATH) if os.path.isdir(os.path.join(DIR_PATH, f))]

def create_new_series():
    new_series = create_new_title.get("1.0", "end-1c").strip()
    if new_series:
        new_dir = os.path.join(DIR_PATH, new_series)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            open_series(new_series)
        else:
            print("Series already exists!")

def open_series(series):
    print(f"Opening series: {series}")
    subprocess.Popen(
        [sys.executable] + ["series.py"] + ["--detached"] + ["--series"] + [series],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    sys.exit()

# GUI Setup
def open_settings():
    settings_menu = ctk.CTkToplevel(root)
    settings_menu.geometry("300x400")
    settings_menu.resizable(False, False)
    settings_menu.title("Penclave Settings")
    settings_menu.grab_set()
    settings_menu.mainloop()

# Main application logic
if "--debug" not in sys.argv:
    pass
    #suppress_console()

# Load series
series_list = load_series()

# Tkinter Setup
root = ctk.CTk()
root.geometry("600x600")
root.title("Penclave")
root.resizable(False, False)

# Title and Subtitle
title = ctk.CTkLabel(root, text="Welcome to Penclave!", font=("Arial", 24, "bold"))
title.pack(pady=10)

subtitle = ctk.CTkLabel(root, text="Select a Series or create a new one!", font=("Arial", 18))
subtitle.pack(pady=10)

# Settings Button
settings_button = ctk.CTkButton(root, text="⚙️", width=40, height=40, command=open_settings, fg_color="transparent", bg_color="transparent")
settings_button.place(x=550, y=7)

# Scrollable Frame for series buttons
container = ctk.CTkScrollableFrame(root, width=550, height=438)
container.pack()

# Create New Series Button & Textbox
create_new_button = ctk.CTkButton(root, width=125, height=40, text="Create!", font=("Arial", 18, "bold"), command=create_new_series)
create_new_button.pack(pady=10, padx=15, side="left")

create_new_title = ctk.CTkTextbox(root, width=475, height=40)
create_new_title.pack(pady=10, padx=15, side="right")

# Create buttons for existing series
for series in series_list:
    series_button = ctk.CTkButton(container, text=series, width=500, height=40, command=lambda sr=series: open_series(sr))
    series_button.pack(pady=5)

# Run the GUI
root.mainloop()