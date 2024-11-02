import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFontDatabase, QIcon
import keyboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Launcher")
        self.setGeometry(100, 100, 300, 50)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        font_id = QFontDatabase.addApplicationFont("FiraCode-Regular.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        else:
            font_family = "Arial"
        self.input_field = QLineEdit(self)
        self.input_field.setAlignment(Qt.AlignCenter)
        self.input_field.setStyleSheet(f"""
            color: white; 
            background-color: rgba(50, 50, 50, 200); 
            font-family: '{font_family}'; 
            font-size: 14pt;
        """)
        self.setCentralWidget(self.input_field)
        self.input_field.returnPressed.connect(self.run_program)
        self.center()

    def center(self):
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()

    def run_program(self):
        program_name = self.input_field.text().strip()
        if program_name:
            try:
                subprocess.Popen(program_name, creationflags=subprocess.CREATE_NO_WINDOW)
            except Exception as e:
                print(f"Kesalahan: {e}")
        self.input_field.clear()

class AppTray:
    def __init__(self, icon_path):
        self.tray_icon = QSystemTrayIcon(QIcon(icon_path))
        self.tray_icon.setVisible(True)
        self.create_context_menu()
        self.tray_icon.activated.connect(self.on_tray_icon_click)
        self.launcher = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_hotkeys)
        self.timer.start(100)

    def create_context_menu(self):
        menu = QMenu()
        exit_action = QAction("Exit")
        exit_action.triggered.connect(self.exit_action)
        menu.addAction(exit_action)
        self.tray_icon.setContextMenu(menu)

    def on_tray_icon_click(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.open_launcher()

    def exit_action(self):
        os._exit(0)

    def open_launcher(self):
        if not self.launcher:
            self.launcher = MainWindow()
            self.launcher.show()
            self.launcher.raise_()
            self.launcher.activateWindow()
        else:
            self.launcher.show()

    def check_hotkeys(self):
        if keyboard.is_pressed('alt+f2'):
            if not self.launcher:
                self.open_launcher()
            else:
                self.launcher.show()

def main():
    app = QApplication([])
    icon_path = "E:\\Developer\\Program\\Python\\run_fzf\\20230315_144251.ico"
    tray = AppTray(icon_path)
    app.exec_()

if __name__ == "__main__":
    main()

