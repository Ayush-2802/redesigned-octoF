import os
import playsound

try:
    music_dir = 'C:\\Users\\Aditi Ayush\\Music'
    songs = os.listdir(music_dir)
    a = enumerate(songs)
    os.startfile(os.path.join(music_dir, songs[0]))
    print(" to veiw song list song list (press s)")
    ch = input(">")
    if ch == "s":
        print (a)
except Exception as g:
    if g == "list index out of range":
        print("no songs found")
    else:
        print("i ran out of songs")
    
