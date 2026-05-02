import time
from threading import Thread, Lock
import sys
import random

lock = Lock()

# warna terminal (ANSI)
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

def sing_song():
    lyrics = [
        ("I want to show you all the finer things in life", 0.07),

        ("So just forget about the world, we young tonight", 0.10),
        ("I'm coming for ya....", 0.08),
        ("I'm coming for ya....\n", 0.08),

        ("'Cause all...", 0.08),
        ("......", 0.23),
        ("I need..", 0.10),
        ("Is a beauty and a beat", 0.13),
        ("Who can make my life complete.....\n\n\n\n\n", 0.15)
    ]

    delays = [0.4, 3.5, 5.5, 10.5, 12.5, 14.0, 16.5, 18.7, 22.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sing_song()