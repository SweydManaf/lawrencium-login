from tkinter import *
from window import MainWindow
from PIL import Image, ImageTk


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('LAWRENCIUM LOGIN')
        self.root.tk.call('source', 'azure.tcl')
        self.root.tk.call('set_theme', 'light')

        # SET BACKGORUND IMAGE
        self.image = ImageTk.PhotoImage(Image.open('assets/Lawrencium.jpg'))
        self.canvas = Canvas(self.root, width=610, height=int(self.root.winfo_screenheight() - 300))
        self.canvas.grid(row=0, column=0)
        self.createImage = self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        # CONFIGURE THE WINDOW
        self.width = 610
        self.height = int(self.root.winfo_screenheight() - 300)
        self.sys_width = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        self.sys_height = int((self.root.winfo_screenheight() / 2) - (self.height / 2))

        self.root.geometry(f'{self.width}x{self.height}+{self.sys_width}+{self.sys_height}')
        self.root.resizable(width=False, height=False)

        # CALL WINDOW
        MainWindow(self.root)

        # START THE APLICATION
        self.root.mainloop()


if __name__ == '__main__':
    Main()
