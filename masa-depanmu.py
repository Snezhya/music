import time
from threading import Thread, Lock
import sys
import random
from threading import Event

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

        i = 0
        while i < len(text):
            if text[i:i+7] == "[pause=":
                j = text.find("]", i)
                pause_time = float(text[i+7:j])
                time.sleep(pause_time)
                i = j + 1
                continue

            sys.stdout.write(color + text[i] + reset)
            sys.stdout.flush()
            time.sleep(delay)
            i += 1

        print()

def idle_animation(stop_event):
    spinner = ["|", "/", "-", "\\"]
    i = 0
    while not stop_event.is_set():
        with lock:
            sys.stdout.write("\r" + spinner[i % len(spinner)])
            sys.stdout.flush()
        time.sleep(0.1)
        i += 1

def sing_lyric(lyric, delay, speed):
    stop_event = Event()
    t = Thread(target=idle_animation, args=(stop_event,))
    t.start()

    time.sleep(delay) 

    stop_event.set()  
    t.join()

    with lock:
        sys.stdout.write("\r ")
        sys.stdout.flush()

    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n\nHabiskan waktu", 0.07),
        ("Hanya bersama dirimu\n\n", 0.09),

        ("Tak terbayangkan jika kita tidak berjumpa", 0.08),
        ("Hanya dirimulah yang buatku semakin cinta...", 0.08),
        ("Don`t far away and i hope you to stay", 0.09),
        ("You`re always make my day and i was like okay yeah\n\n", 0.08),

        ("Ta..ta..ta tak perlu kau mengingat semua yang tlah berlalu....", 0.07),
        ("Cukup bersyukur bahwa diriku masa depanmmu", 0.08),
        ("Semua akan aku berikan hanya untukmu u..u..u..u", 0.10),
        ("Hanya satu..u..u..u", 0.08),
        ("Hanya kamu\n\n", 0.08),
    ]

    delays = [0.2, 0.5, 0.2, 0.2, 0.3, 0.5, 0.5, 0.7, 0.6, 0.5, 0.5]

    last_time = 0

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]

        wait_time = delays[i] - last_time
        if wait_time > 0:
            time.sleep(wait_time)

        animate_text(lyric, speed)
        last_time = delays[i]

if __name__ == "__main__":
    sing_song()