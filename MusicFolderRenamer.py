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

