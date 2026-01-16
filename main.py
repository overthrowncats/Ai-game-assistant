import tkinter as tk
from tkinter import messagebox, simpledialog
import pyautogui
import cv2
import numpy as np
import time
import psutil

class UniversalGameBeater:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PC Scenario Engine v2.0")
        self.root.geometry("450x350")
        self.root.configure(bg="#2c3e50")

        # The Legal and Safety Terms
        self.tos_text = (
            "USER AGREEMENT:\n"
            "1. Prohibited in competitive online multiplayer.\n"
            "2. Use only in single-player/educational environments.\n"
            "3. User assumes all risk for account bans or penalties."
        )
        
        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.root, text="SCENARIO ANALYZER", font=("Courier", 18, "bold"), fg="#ecf0f1", bg="#2c3e50")
        title.pack(pady=10)

        tos_box = tk.Label(self.root, text=self.tos_text, justify="left", fg="#e74c3c", bg="#2c3e50", font=("Arial", 9, "italic"))
        tos_box.pack(pady=10)

        self.btn_launch = tk.Button(self.root, text="CHOOSE RUNNING GAME", command=self.run_engine, 
                                   bg="#27ae60", fg="white", font=("Arial", 10, "bold"), padx=20)
        self.btn_launch.pack(pady=20)

    def check_online_status(self, process_name):
        """Checks if the game has active network sockets."""
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == process_name.lower():
                try:
                    return len(proc.connections()) > 0
                except (psutil.AccessDenied, psutil.NoSuchProcess):
                    return False
        return False

    def run_engine(self):
        game_name = simpledialog.askstring("Target Game", "Enter the .exe name (e.g., 'Cyberpunk2077.exe'):")
        
        if not game_name:
            return

        # Warning Logic with your specific phrasing
        if self.check_online_status(game_name):
            warning_msg = (
                f"THIS GAME IS ONLINE, ARE YOU SURE IT ISN'T COMPETITIVE?\n\n"
                f"WARNING: Some games/apps could ban you for using these types of cheats."
            )
            confirm = messagebox.askyesno("SECURITY ALERT", warning_msg)
            if not confirm:
                return

        level_name = simpledialog.askstring("Level", "Enter Level ID/Scenario:")
        self.start_logic_loop(game_name)

    def start_logic_loop(self, game_name):
        messagebox.showinfo("Running", f"Engine active. Press CTRL+C in terminal to emergency stop.")
        # Logic loop would go here (Screen capture -> Decision -> Input)
        print(f"Monitoring {game_name} for optimal jump scenarios...")

if __name__ == "__main__":
    app = UniversalGameBeater()
    app.root.mainloop()
