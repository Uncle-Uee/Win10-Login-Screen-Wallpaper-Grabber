"""

Created by: Uee
Created on: 29 June 2019

License:
What License???

Description:
Have you ever wanted a copy of your Windows 10 Login Screen Wallpaper?
With this Script, you can. This Script will Copy the Windows Login Screen Wallpapers to your Pictures Directory.
"""

import os
import shutil

# Folder of the User that is Logged in.
USER = os.path.expanduser("~")

# Path of the Login Screen Wallpapers.
PATH = "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"

# Complete Path to the Login Screen Wallpapers.
WALLPAPER_PATH = USER + PATH

# Directory to Save Login Screen Wallpapers.
SAVE_DIRECTORY = USER + "\\Pictures\\Windows Login Wallpapers\\"

# Minimum Size of the Wallpapers to Copy.
MIN_FILE_SIZE = 100000

# Maximum Size of the Wallpapers to Copy.
MAX_FILE_SIZE = 5000000


def is_valid_directory(path = ""):
	"""
	Check if the Path is a Valid Directory.

	:param path: String Path Location of a Folder.
	:return: True or False.
	"""
	if os.path.isdir(path):
		return True
	return False


def list_files(path = ""):
	"""
	List the Files, of a Directory.

	:param path: String Path Location of the Folder.
	:return: List of Files.
	"""
	if is_valid_directory(path):
		return os.listdir(path)
	return []


def get_wallpapers(path = "", minimum_size = 100000, maximum_size = 500000, extension = ".jpg"):
	"""
	Get Wallpaper Files within a Folder within a Specified Size Range i.e Size is in KB.

	:param path: String Path Location of the Folder.
	:param minimum_size: Minimum Size of the File.
	:param maximum_size: Maximum Size of the File.
	:param extension: File Extension.
	"""

	if not is_valid_directory(SAVE_DIRECTORY):
		os.mkdir(SAVE_DIRECTORY)

	for file in list_files(path):
		if minimum_size <= os.path.getsize(path + "\\" + file) <= maximum_size:
			print("File Stored : " + file)
			shutil.copy(path + file, SAVE_DIRECTORY + file + extension)

	os.system("pause")


if __name__ == "__main__":
	try:
		get_wallpapers(WALLPAPER_PATH, MIN_FILE_SIZE, MAX_FILE_SIZE, extension = input("File Extension i.e .jpg :\n"))
	except Exception as error:
		print(error)
