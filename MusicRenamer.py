import os

artistPath = ""

while artistPath == "":   
        artistPath = input("Enter folder location in system directory (eg- /users/username/desktop/foldername): ")

        try:
            os.listdir(artistPath)

        except:
            print("Invalid filepath, try again")
            artistPath = ""

artistPath.strip()

try:
        location = artistPath + "/" + ".DS_Store"
        os.remove(location)

except:
        print("No rubbish files found for deletion")

sorted_artists = sorted(os.listdir(artistPath))

print(sorted_artists)

for artist in sorted_artists:
        
        albumPath = artistPath + "/" + artist

        print(albumPath)
        os.chdir(albumPath)

        try:
                location = albumPath + "/" + ".DS_Store"
                os.remove(location)

        except:
               print("No rubbish files found for deletion")

        sorted_albums = sorted(os.listdir(albumPath))
        print(sorted_albums)

        for album in sorted_albums:
                
                songPath = albumPath + "/" + album

                print(songPath)
                os.chdir(songPath)

                sorted_songs = sorted(os.listdir(songPath))

                for songName in sorted_songs:
                        newName = songName[5:len(songName)]

                        print(newName)

                        os.rename(songName, newName)
        


