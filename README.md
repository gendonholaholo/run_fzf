# Run_fzf_gos


## Features

- **System Tray Icon**: The application runs in the system tray, providing easy access.
- **Keyboard Shortcut**: Launch the input field using the `Alt + F2` hotkey.
- **Input Field**: Type the name of the program you want to run and hit Enter.
- **Esc Key**: Close the input field by pressing the Escape key.
- **Custom Font**: Utilizes the Fira Code font for the input field (with fallback to Arial).

## Requirements

- Python 3.x
- PyQt5
- keyboard

You can install the required packages using pip:

```bash
pip install PyQt5 keyboard
```

## Usage

  1.  Run the Script: Execute the script using Python.
    ```
python your_script_name.py
    ```
  2.  Access the Launcher: Click the system tray icon or press `Alt + F2` to open the input field.
  3.  Run a Program: Type the name of the executable (e.g., notepad, calc) and press Enter.
  4.  Exit the Application: Right-click the system tray icon and select "Exit" or press Esc when the input field is open.

## Customization

- **Change the path of the icon**: Modify the `icon_path` variable in the main() function to
customize the system tray icon.
- **Modify the input field style**: Modify the styles in the MainWindow class for different visual
appearances.
- **Ensure that FiraCode-Regular.ttf font file is available**: Ensure that the FiraCode-Regular.ttf
font file is in the same directory or update the path as needed.
