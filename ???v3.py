import time
from threading import Thread, Lock
import sys
import random

lock = Lock()

colors = [
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
]
reset = "\033[0m"

def animate_text(text, delay=0.05):
    with lock:
        color = random.choice(colors)
        for char in text:
            sys.stdout.write(color + char + reset)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

## 🔥 LOAD ASCII DARI FILE
#def show_ascii(file_path):
#    try:
#        with open(file_path, "r") as f:
#            art = f.read()
#            print(art)
#    except:
#        print("ASCII file ga ketemu, bego 😹 (cek path lu)")
#

def show_ascii(file_path):
    try:
        with open(file_path, "r") as f:
            print(f.read())
    except:
        print("file ga ketemu 😹")

show_ascii("/home/snezhya/code/hu_tao_ASCII.txt")

def sing_song():
    lyrics = [
        ("\nAll I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.04),
        ("Is somebody to you", 0.04),
        ("All I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.04),
        ("Is somebody to you", 0.04),
        ("Everybody's tryna be a billionaire", 0.05),
        ("But every time I look at you, I just don't care", 0.04),
        ("Cause all I wanna be, yeah, all I ever wanna be, yeah, yeah", 0.05),
        ("Is somebody to youuuuu 🎶", 0.04)
    ]

    delays = [0.3, 3.5, 5.3, 8.5, 10.0, 12.5, 14.7, 18.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    print("\n👏 END OF SHOW 👏")

if __name__ == "__main__":
    loading_intro()
    sing_song()