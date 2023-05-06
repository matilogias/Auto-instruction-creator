# project_loader_module.py

import os
import json
import tkinter as tk
from tkinter import messagebox

def load_project():
    project_folders = []
    if not os.path.exists("projects"):
        return None

    for folder in os.listdir("projects"):
        if os.path.isdir(os.path.join("projects", folder)):
            project_folders.append(folder)

    if not project_folders:
        messagebox.showinfo("Informacja", "Folder with projects does not exist.")
        return None

    project_window = tk.Toplevel()
    project_window.title("Wybierz projekt")

    label = tk.Label(project_window, text="Select project folder:")
    label.pack(padx=10, pady=10)

    project_var = tk.StringVar(project_window)
    project_var.set(project_folders[0])

    project_menu = tk.OptionMenu(project_window, project_var, *project_folders)
    project_menu.pack(padx=10, pady=10)

    def confirm_selection():
        selected_project = project_var.get()
        project_window.destroy()
        project_window.result = selected_project

    confirm_button = tk.Button(project_window, text="Select", command=confirm_selection)
    confirm_button.pack(padx=10, pady=10)

    project_window.grab_set()
    project_window.wait_window()

    return project_window.result
