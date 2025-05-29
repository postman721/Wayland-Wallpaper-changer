import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.setStyleSheet("""
            * {
                color: #ffffff;
                background-color: #2f2e2d;
                border: 2px solid #353535;
                border-radius: 3px;
                font-size: 12px;
            }
            *:selected {
                background-color: #125c8c;
            }
        """)
        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Choose wallpaper",
            "/usr/share/postx-wallpapers",  # Default path
            "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)",
            options=options
        )

        if fileName:
            self.set_wallpaper_wayland(fileName)
        else:
            sys.exit()

    def set_wallpaper_wayland(self, file_path):
        home = os.path.expanduser("~")
        wall_script_dir = os.path.join(home, ".wall")
        wall_script_path = os.path.join(wall_script_dir, "wall.sh")

        os.makedirs(wall_script_dir, exist_ok=True)

        # Write swaybg command to script
        with open(wall_script_path, "w") as f:
            f.write(f"#!/bin/bash\n")
            f.write(f"pkill swaybg\n")  # Kill any previous background process
            f.write(f"swaybg -i \"{file_path}\" -m fill &\n")

        os.chmod(wall_script_path, 0o755)  # Make it executable

        # Optional: run it now
        subprocess.Popen(["bash", wall_script_path])

        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
