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

def sing_song():
    lyrics = [
        ("Habiskan waktu", 0.06),
        ("Hanya bersama dirimu\n\n", 0.09),

        ("Tak terbayangkan jika kita tidak berjumpa", 0.08),
        ("Hanya dirimulah yang buatku semakin cinta", 0.08),
        ("Don`t far away and i hope you to stay", 0.10),
        ("you`re always make my day and i was like okay yeah\n\n", 0.08),

        ("Ta..ta..ta tak perlu kau mengingat semua yang tlah berlalu", 0.10),
        ("Cukup bersyukur bahwa diriku masa depanmmu", 0.23),
        ("Semua akan aku berikan hanya untukmu u..u..u..u", 0.10),
        ("Hanya satu..u..u..u", 0.13),
        ("Hanya kamu\n\n", 0.15),
    ]

    delays = [0.4, 1.5, 3.0, 6.5, 11.5, 16.5, 17.5, 18.7, 22.5, 25.0, 28.6, 36.6, 43.0, 44.0, 46.0]

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