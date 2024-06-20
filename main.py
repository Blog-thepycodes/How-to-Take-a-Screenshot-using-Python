import tkinter as tk
from tkinter import filedialog
import pyautogui
from datetime import datetime
 
 
class ScreenshotApp:
   def __init__(self, root):
       self.root = root
       self.root.title("Screenshot App - The Pycodes")
 
 
       self.canvas = tk.Canvas(root, width=300, height=200)
       self.canvas.pack()
 
 
       self.create_widgets()
 
 
   def create_widgets(self):
       self.screenshot_button = tk.Button(
           text="Take Screenshot", command=self.take_screenshot, bg="blue", fg="white"
       )
       self.canvas.create_window(150, 100, window=self.screenshot_button)
 
 
   def take_screenshot(self):
       try:
           # Hide the window to capture only the desktop
           self.root.iconify()
 
 
           # Capture screenshot
           screenshot = pyautogui.screenshot()
 
 
           # Show the window again
           self.root.deiconify()
 
 
           # Ask user for file path
           file_path = filedialog.asksaveasfilename(
               defaultextension=".png",
               filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
           )
 
 
           # Save screenshot with a timestamp in the filename
           timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
           file_path_with_timestamp = f"{file_path}_{timestamp}.png"
           screenshot.save(file_path_with_timestamp)
 
 
           # Inform the user about the successful capture
           self.show_message("Screenshot captured successfully!")
       except Exception as e:
           # Inform the user if an error occurs
           self.show_message(f"Error: {e}")
 
 
   def show_message(self, message):
       # Display a message to the user
       popup = tk.Toplevel(self.root)
       popup.title("Message")
       label = tk.Label(popup, text=message)
       label.pack(padx=10, pady=10)
       ok_button = tk.Button(popup, text="OK", command=popup.destroy)
       ok_button.pack(pady=10)
 
 
if __name__ == "__main__":
   root = tk.Tk()
   app = ScreenshotApp(root)
   root.mainloop()
