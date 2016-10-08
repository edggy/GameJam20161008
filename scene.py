import tkinter as tk

'''
Scene is the top half of the window that shows the background and has slots to place chacters.
'''


class Scene(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(self, parent)
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Scene(master=root)
    app.mainloop()
        
        

