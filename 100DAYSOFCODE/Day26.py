from replit import audio
import os, time


def play():
    source = audio.play_file('audio.wav')
    source.paused = False
    while True:
        play_back = int(input('press 5 to go back to main menu:'))
        if play_back == 5:
            source.paused = True
            return
        else:
            continue


while True:
    print("My Pod Music Player")
    time.sleep(1)
    os.system('clear')
    print("""
  Press 1 to Play
  Press 2 to exit
  """)
    press = int(input())
    os.system('clear')
    if press == 1:
        print("Playing some proper tunes")
        play()
    if press == 2:
        break
    else:
        continue
