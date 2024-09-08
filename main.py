import pygame
from time import sleep

def play_audio(audio_sound, times, audio_delay):
    for _ in range(times):
        audio_sound.play()
        sleep(audio_delay)

pygame.mixer.init()

audio_file = 'sound.mp3'
sound = pygame.mixer.Sound(audio_file)

while True:
    try:
        delay = float(input("Enter the delay between plays (in seconds): "))
        count = int(input("Enter amount of times to play: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

try:
    play_audio(sound, count, delay)
except KeyboardInterrupt:
    print("Bye!")
finally:
    pygame.mixer.quit()