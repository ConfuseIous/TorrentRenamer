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

sorted_files = sorted(os.listdir(path))

print("done")
print(sorted_files)

newname = input("What should the files be named? (eg- Breaking Bad S01E will return Breaking Bad S01E01...): ")
ext = input("What is the file format? (mkv/mp4/jpg/png/etc): ")

os.chdir(path)

for index, filename in enumerate(sorted_files, 1):
        
        name = f"{newname}{index:02d}.{ext}"

        print("renaming " + filename + "to " + name) 

        os.rename(filename, name)
