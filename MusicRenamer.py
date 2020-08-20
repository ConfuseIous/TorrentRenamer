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

try:
        location = path + "/" + ".DS_Store"
        os.remove(location)

except:
        print("No rubbish files found for deletion")

for f in os.listdir(path):
    print(f)

sorted_artists = sorted(os.listdir(path))


print(sorted_artists)

for folder in sorted_folders:
        
        newPath = path + "/" + folder

        print(newPath)
        os.chdir(newPath)

        try:
                location = newPath + "/" + ".DS_Store"
                os.remove(location)

        except:
               print("No rubbish files found for deletion")

        sorted_albums = sorted(os.listdir(newPath))

        for filename in sorted_albums:
                count = len(filename)
                print(filename)
                newName = filename[5:count]

                print(newName)

                #os.rename(filename, newName)
        


