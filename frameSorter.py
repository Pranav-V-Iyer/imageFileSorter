import os
import shutil
from tkinter import Tk, PhotoImage, Canvas

loopPoint = 0

folder_path = 'imageFolder'
image_paths = []

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        image_path = os.path.join(folder_path, filename)
        image_paths.append(image_path)

def move_file(key):
    global loopPoint
    if loopPoint < len(image_paths):
        source_path = image_paths[loopPoint]
        folder_path_1 = "folder_1"
        folder_path_2 = "folder_2"
        if key == "1":
            destination = folder_path_1
        elif key == "2":
            destination = folder_path_2
        else:
            return
        shutil.move(source_path, destination)
        loopPoint += 1
        update_ui()

def update_ui():
    image_path = image_paths[loopPoint]
    img = PhotoImage(file=image_path)
    canvas.itemconfig(image_item, image=img)
    canvas.image = img

def on_key(event):
    move_file(event.char)

root = Tk()
root.title("Image Mover")

image_path = image_paths[loopPoint]
img = PhotoImage(file=image_path)
canvas = Canvas(root, width=img.width(), height=img.height())
image_item = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.pack()

root.bind("<Key>", on_key)


root.mainloop()
