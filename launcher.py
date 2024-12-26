import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x600")
root.title("Placeholder")
root.resizable(False, False)

# Title and Subtitle
title = ctk.CTkLabel(root, text="Welcome to Penclave!", font=("Arial", 24, "bold"))
title.pack(pady=10)

subtitle = ctk.CTkLabel(root, text="Select a Series or create a new one!", font=("Arial", 18))
subtitle.pack(pady=10)

# Add settings icon button
def open_settings():
    settings_menu = ctk.CTkToplevel(root)
    settings_menu.geometry("300x400")
    settings_menu.resizable(False, False)
    settings_menu.title("Penclave Settings")

    settings_menu.grab_set()

    settings_menu.mainloop()

settings_button = ctk.CTkButton(root, text="⚙️", width=40, height=40, command=open_settings, fg_color="transparent", bg_color="transparent")
settings_button.place(x=550, y=7)

# Scrollable Frame
container = ctk.CTkScrollableFrame(root, width=550, height=438)
container.pack()

# Buttons and text box
create_new_button = ctk.CTkButton(root, width=125, height=40, text="Create!", font=("Arial", 18, "bold"))
create_new_button.pack(pady=10, padx=15, side="left")

create_new_title = ctk.CTkTextbox(root, width=475, height=40)
create_new_title.pack(pady=10, padx=15, side="right")

root.mainloop()