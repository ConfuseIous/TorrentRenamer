##########################################################
#                                                        # 
# TorrentRenamer by Karandeep Singh (ConfuseIous)        #
#                                                        # 
# https://github.com/ConfuseIous/TorrentRenamer          #
#                                                        # 
# Provided under the MIT License. See LICENSE.txt        # 
#                                                        # 
# DISCLAIMER: This script has only been tested on macOS. #
# Use on other systems at your own risk.                 #
#                                                        #
##########################################################

import os

path = ""

while path == "":
        path = input("Enter folder location in system directory (eg- /users/username/desktop/foldername): ")

        try:
            os.listdir(path)

        except:
            print("Invalid filepath, try again")
            path = ""

path.strip()

# macOS creates a .DS_Store file, which may cause issues, thus it is removed
try:
        location = path + "/" + ".DS_Store"
        os.remove(location)
except:
        pass

ext = ""
for index, file in enumerate(os.listdir(path)):
        if index == 0:
                ext = os.path.splitext(file)[1]
        elif os.path.splitext(file)[1] != ext:
                print("Not all files have the same extension. TorrentRenamer will now quit. Please remove any extra files and run TorrentRenamer again.")
                quit()

sorted_files = sorted(os.listdir(path)) 

newname = input("What should the files be named? (eg- Breaking Bad S01E will return Breaking Bad S01E01...): ")

os.chdir(path)

for index, filename in enumerate(sorted_files, 1):
        name = f"{newname}{index:02d}{ext}"
        os.rename(filename, name)
        print("Renamed " + filename + " to " + name)
