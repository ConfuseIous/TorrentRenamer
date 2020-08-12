import os

path = ""

while path == "":
        path = input("Enter folder location in system directory (eg- /users/username/desktop/foldername): ")

        try:
            os.listdir(path)

        except:
            print("Invalid filepath, try again")
            path = ""


for f in os.listdir(path):
    print(f)

newname = input("What should the files be named? (eg- Breaking Bad S01E will return Breaking Bad S01E01...): ")
ext = input("What is the file format (mkv/mp4/jpg/png/etc)")

os.chdir(path)

index = 1

for filename in os.listdir(path):
        print(filename)
        if index < 10:
                name = newname + "0" + str(index) + "." + ext
        else:
                name = newname + str(index) + "." + ext

        os.rename(filename, name)
        index += 1

