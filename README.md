# Wayland-Wallpaper-changer
Wallpaper changer for wayland

A minimal PyQt5-based GUI tool for setting wallpapers on Wayland compositors (like Labwc or Sway) using swaybg.
Features

    Simple PyQt5 GUI to choose a wallpaper

    Automatically sets it using swaybg

    Terminates existing background processes for a clean switch

    Generates a reusable wallpaper script at ~/.wall/wall.sh


### Requirements
Runtime Dependencies (Debian/Ubuntu)

### Install required packages using:

sudo apt update
sudo apt install python3 python3-pyqt5 swaybg

### Run the script:

python3 wallpaper_changer.py

Or:

./wallpaper_changer.py

A file dialog will appear. Select your desired image (.png, .jpg, .jpeg, .bmp), and it will instantly become your wallpaper using swaybg.
Script Output

The wallpaper is applied via a script saved to:

~/.wall/wall.sh

### Autostart

Is possbile add it according to your env. 
You will want to execute: 

bash ~/.wall/wall.sh
