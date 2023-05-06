# Auto instruction creator

Auto instruction creator Tool is a simple GUI-based application that allows users to take screenshots of specific areas on their screen, add descriptions to each screenshot, and save the collection as a Microsoft Word document. It also supports loading and editing existing projects(project is folder with screanshots descriptions descriptions). The tool was created because I needed a way to quickly create instructions fo rmy clients, and I wanted to automate the process as much as possible. Tool is created mostly using GPT-3.5 and GPT-4 models. I wanted to share this tool with the community in case anyone else finds it useful.
This tool is working on only windows and takes screenshots of the primary monitor only.

## Features

- Take screenshots by clicking on the screen
- Mark place on screenshot where you clicked with red dot
- Add descriptions to each screenshot
- Save the collection of screenshots and descriptions as a Word document
- Load and edit existing projects (screanshots with descriptions)

## Installation

1. Ensure you have Python 3.7 or later installed on your system.
2. Install the required dependencies using pip:
pip install -r requirements.txt

The dependencies include:

- numpy
- opencv-python
- pyautogui
- python-docx
- pillow
- pypiwin32
- mouse
- keyboard

3. Clone or download the repository to your local machine.

## Usage

1. Navigate to the folder containing the script.
2. Run the script with the following command:
python main.py
3. Enter a project name, or open an existing project using the "Open Project" button.
4. Click "Start/Stop Screenshot Mode" to begin taking screenshots. Click on the desired areas of the screen while in screenshot mode.
5. Click "Load/Edit Images" to view and edit the descriptions for each screenshot.
6. Save the project as a Word document by clicking "Save to Word."

## License

This project is licensed under the [MIT License](LICENSE).
