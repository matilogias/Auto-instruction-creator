import os
import json
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def display_image_table(screenshots_folder, image_files, descriptions):
    json_file = os.path.join(screenshots_folder, "descriptions.json")

    # Load the descriptions from the JSON file
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            descriptions = json.load(f)

    def on_image_click(event, index):
        nonlocal image_files, screenshots_folder
        image_path = os.path.join(screenshots_folder, image_files[index])
        full_image = Image.open(image_path)

        # Create a new window to display the full-size image
        top = Toplevel()
        top.title(image_files[index])
        top.attributes('-fullscreen', True)

        # Resize the image to fit the window
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        img_w, img_h = full_image.size
        scale = min(w/img_w, h/img_h)
        new_size = (int(img_w*scale), int(img_h*scale))
        full_image = full_image.resize(new_size)

        # Display the full-size image in the new window
        full_image = ImageTk.PhotoImage(full_image)
        label = Label(top, image=full_image)
        label.image = full_image
        label.pack(fill=BOTH, expand=1, padx=5, pady=5)

        # Destroy the window when it is closed
        def close_window(event):
            top.destroy()
        label.bind("<Button-1>", close_window)

        top.mainloop()

    def on_accept_click():
        nonlocal image_entries, descriptions, table_window
        for index, entry in enumerate(image_entries):
            descriptions[image_files[index]] = entry.get("1.0", "end-1c")
        table_window.destroy()

    table_window = Toplevel()
    table_window.title("Add descriptions")

    # Set the size of the window and add a scrollbar
    table_window.geometry("800x600")
    table_window.bind("<MouseWheel>", lambda event: images_canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    
    # Create a frame for the information label
    info_frame = Frame(table_window, pady=10)
    info_frame.pack(side=TOP, fill=X)

    # Create a label with information for the user
    info_label = Label(info_frame, text="Click on the thumbnail to display the image in full size. Enter the image description in the text box.")
    info_label.pack()

    # Create scrollable frame to hold the images and descriptions
    main_frame = Frame(table_window)
    main_frame.pack(fill=BOTH, expand=1)

    scroll = Scrollbar(main_frame, orient=VERTICAL)
    scroll.pack(side=RIGHT, fill=Y)

    images_canvas = Canvas(main_frame, yscrollcommand=scroll.set)
    images_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scroll.config(command=images_canvas.yview)

    images_frame = Frame(images_canvas)
    images_canvas.create_window((0, 0), window=images_frame, anchor="nw")

    # Display a message if the screenshots folder does not exist
    if not os.path.exists(screenshots_folder):
        message_label = Label(images_frame, text="Folder with screenshots does not exist.")
        message_label.pack(padx=5, pady=5)
        images_canvas.config(scrollregion=images_canvas.bbox("all"))
        return descriptions

    # Create the image and description table
    image_entries = []

    for index, image_file in enumerate(image_files):
        image_path = os.path.join(screenshots_folder, image_file)
        image = Image.open(image_path)
        thumbnail_size = (400, 400)
        image.thumbnail(thumbnail_size)
        image = ImageTk.PhotoImage(image)

        # Display the image thumbnail with a click event to open the full image
        image_label = Label(images_frame, image=image)
        image_label.image = image
        image_label.grid(row=index, column=0, padx=5, pady=5)
        image_label.bind("<Button-1>", lambda event, index=index: on_image_click(event, index))

        # Display the description in a text box
        description = descriptions.get(image_file, "")
        entry = Text(images_frame, width=50, height=5, wrap=WORD)
        entry.insert(INSERT, description)
        entry.grid(row=index, column=1, padx=5, pady=5)
        image_entries.append(entry)

    # Update the scroll region after the images and descriptions have been added
    images_frame.update_idletasks()
    images_canvas.config(scrollregion=images_canvas.bbox("all"))

    # Add the accept button
    accept_button = Button(table_window, text="Accept", command=on_accept_click)
    accept_button.pack(side=RIGHT, padx=5, pady=5)

    table_window.mainloop()

    return descriptions
