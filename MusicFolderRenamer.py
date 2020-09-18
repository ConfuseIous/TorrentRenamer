import os

##REMOVE BLINK-182 FROM FOLDER BEFORE RUNNING THIS

artistPath = "/users/karandeepsingh/desktop/music"

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
        os.chdir(albumPath)

        try:
                location = albumPath + "/" + ".DS_Store"
                os.remove(location)

        except:
               print("No rubbish files found for deletion")

        sorted_albums = sorted(os.listdir(albumPath))

        for album in sorted_albums:
                
               rem_i = album.find("-")

               if rem_i != -1:
                       end = len(album)
                       new_str = album[rem_i+1:end]
                       new_str.strip
                       os.rename(album, new_str)


        


