# Win10-Login-Screen-Wallpaper-Grabber
Save a copy of your Windows 10 Login Screen Wallpaper.

# Creating an Exe
You need to install PyInstaller for Python.
You can use the following command "pyinstaller.exe --onefile --windowed --console --icon=icon.ico save_login_wallpaper.py" to create an executable from within the Terminal or CMD.

# Not Creating an Exe
You can run the Script without compiling it to an exe, by just opening it as usual 😎.

# User Input
You only need to pass a String Value for the extension of the Wallpapers for example ".jpg".

# Modification
You can Edit the Script Variables within the script to change the Save Location of Login Screen Wallpapers as well as the Minimum and Maximum Size Range of the Wallpapers you wish to make a copy of.

Default Values:
SAVE_DIRECTORY = USER + "//Pictures//Windows Login Wallpapers//" , where USER = "c://user//yourname"
MIN_FILE_SIZE = 100000, where the value is in bytes in this case 100kb.
MAX_FILE_SIZE = 5000000, where the value is in bytes in this case 5mb.
