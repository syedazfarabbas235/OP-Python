import tkinter as tk
from drawing.pen import Pen
from App.app import App

if __name__ == "__main__":
    # Create Tkinter window
    root = tk.Tk()
    root.title("Turtle Drawing App")

    # Pass Tkinter root to Pen
    pen = Pen(root)

    # Create App with pen
    application = App(pen)

    
    # Run commands (drawing will happen here)
    application.run_square_only()
    application.run_zigzag_only()
    #application.run()

    # Start Tkinter event loop
    root.mainloop()
