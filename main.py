from tkinter import *
from tkinter import ttk
import datetime 
from PIL import Image,ImageTk
from rembg import remove
import os
from tkinter import filedialog



#Create the main window wizzard.
root = Tk()


# control the size of the wizzard.
root.geometry('250x350')
# change the wizzard icon.
root.iconbitmap('img/myicon.ico')
root.title('Image Background Remover Py')

# ============== Main frame =============== 
F1 = Frame(root, bg='silver', width=250, height=350, relief=GROOVE)
F1.place(x=1, y=1)

def process_files(file_paths):
    # Add your file processing logic here
    print("Processing file...")
    i = 0
    for file_path in file_paths:
       # Processing the image
        input = Image.open(file_path)
        print(input.mode)
        rgb_img = input.convert('RGB')
        print(rgb_img.mode) 
        
        # Removing the background from the given Image 
        output = remove(rgb_img) 
        
        #Saving the image in the given path
        file_name, file_extension = os.path.splitext(file_path)
        print(file_name + "_bgremoved" + file_extension)
        output.save(file_name + "_bgremoved" + file_extension, "PNG")
        i += 1
    L3_title = Label(F1, width=30, text=f"{i}  images procecced.")
    L3_title.place(x=20, y=250)
    print(str(i) + "   were Image procecced.")



def browse_files():
    global file_paths
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("All files", "*.*"), ("png files", "*.png"),("Jpeg files", "*.jpg")])
    number_of_items = len(file_paths)
    L2_title = Label(F1, width=30, text=f"You selects: {number_of_items} images")
    L2_title.place(x=20, y=150)


# Create a button to browse and select files
L_title = Label(F1, width=30, bg="#526E75", fg="white", text="Choose files and remove BG")
L_title.place(x=15, y=50)
browse_button  = Button(F1, text="Browse Files", command=browse_files)
browse_button.place(x=85, y=90)


rem_button  = Button(F1, text="Process images", command=lambda: process_files(file_paths))
rem_button.place(x=75, y=200)

# L2_title = Label = Label(F1, width=30)


# Loop for making the wizzard live.
root.mainloop()
