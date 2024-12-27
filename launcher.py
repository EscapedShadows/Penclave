import customtkinter as ctk
import os
import sys
import subprocess

# Global settings
DEBUG_MODE = "--debug" in sys.argv
DIR_PATH = r"userdata\workspaces"

# Function to suppress the console window (Windows)
def suppress_console():
    if sys.platform.startswith("win") and "--detached" not in sys.argv:
        subprocess.Popen(
            [sys.executable] + sys.argv + ["--detached"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sys.exit()

# Debug helper functions
def debug(content):
    if DEBUG_MODE:
        print(content)

def decoy_debug(content):
    pass

debug = debug if DEBUG_MODE else decoy_debug

# Workspaces management
def load_workspaces():
    debug("Loading workspaces...")
    return [f for f in os.listdir(DIR_PATH) if os.path.isdir(os.path.join(DIR_PATH, f))]

def create_new_workspace():
    new_workspace = create_new_title.get("1.0", "end-1c").strip()
    if new_workspace:
        new_dir = os.path.join(DIR_PATH, new_workspace)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            debug(f"Created new workspace: {new_workspace}")
            open_workspace(new_workspace)
        else:
            debug("Workspace already exists!")

def open_workspace(workspace):
    debug(f"Opening workspace: {workspace}")

# GUI Setup
def open_settings():
    settings_menu = ctk.CTkToplevel(root)
    settings_menu.geometry("300x400")
    settings_menu.resizable(False, False)
    settings_menu.title("Penclave Settings")
    settings_menu.grab_set()
    settings_menu.mainloop()

# Main application logic
if not DEBUG_MODE:
    suppress_console()

# Load workspaces
workspaces = load_workspaces()

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

# Scrollable Frame for workspace buttons
container = ctk.CTkScrollableFrame(root, width=550, height=438)
container.pack()

# Create New Workspace Button & Textbox
create_new_button = ctk.CTkButton(root, width=125, height=40, text="Create!", font=("Arial", 18, "bold"), command=create_new_workspace)
create_new_button.pack(pady=10, padx=15, side="left")

create_new_title = ctk.CTkTextbox(root, width=475, height=40)
create_new_title.pack(pady=10, padx=15, side="right")

# Create buttons for existing workspaces
for workspace in workspaces:
    workspace_button = ctk.CTkButton(container, text=workspace, width=500, height=40, command=lambda ws=workspace: open_workspace(ws))
    workspace_button.pack(pady=5)

# Run the GUI
root.mainloop()