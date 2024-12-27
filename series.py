import customtkinter as ctk
import os
import sys
import subprocess

# Function to suppress the console window (Windows)
def suppress_console():
    if sys.platform.startswith("win") and "--detached" not in sys.argv:
        subprocess.Popen(
            [sys.executable] + sys.argv + ["--detached"],
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        sys.exit()

# Find series argument dynamically
series = None
for i, arg in enumerate(sys.argv):
    if arg == "--series" and i + 1 < len(sys.argv):
        series = sys.argv[i + 1]  # Get the series value after the flag
        break

if series is None:
    print("Series argument is missing!")
    sys.exit()

DIR_PATH = r"userdata\series"

# Main application logic
if "--debug" not in sys.argv:
    suppress_console()

# Print the series for debugging
print(f"Series: {series}")

books = os.listdir(os.path.join(DIR_PATH, series))

print(books)