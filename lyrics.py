import time
from playsound import playsound
import threading

# for playing note.wav file

def play_audio():
    playsound('blue song audio.mp3')
    

def print_lirik():
    lirik = [
        ("", 5, 0.0),
        ("Your morning eyes, I could stare like watching stars", 2, 0.1),
        ("I could walk you by, and I'll tell without a thought", 1, 0.1),
        ("You'd be mine, would you mind if I took your hand tonight?", 1, 0.1),
        ("Know you're all that I want this life", 1, 0.1),
        ("", 2, 0.0),
        ("", 2, 0.07),
        ("I'll imagine we fell in love", 1, 0.05),
        ("I'll nap under moonlight skies with you", 1.5, 0.05),
        ("I think I'll picture us, you with the waves", 1.2, 0.07),
        ("The ocean's colors on your face", 0.8, 0.09),
        ("I'll leave my heart with your air", 1, 0.1),
        ("So let me fly with you", 1, 0.1),
        ("Will you be forever with me?", 1.9, 0.1),
        ("", 10, 0.0),
        ("", 2, 0.06),
        ("My love will always stay by you", 3, 0.1),
        ("I'll keep it safe, so don't you worry a thing", 1.2, 0.09),
        ("I'll tell you I love you more", 1.5, 0.06),
        ("It's stuck with you forever, so promise you won't let it go", 1, 0.1),
        ("I'll trust the universe will always bring me to you", 1, 0.09),
        ("", 2, 0.0),
        ("", 1, 0.04),
        ("I'll imagine we fell in love", 1, 0.05),
        ("I'll nap under moonlight skies with you", 1.5, 0.05),
        ("I think I'll picture us, you with the waves", 1.1, 0.07),
        ("The ocean's colors on your face", 0.8, 0.09),
        ("I'll leave my heart with your air", 1, 0.1),
        ("So let me fly with you", 1, 0.1),
        ("Will you be forever with me?", 1.9, 0.1),
    ]

    for teks, delay_baris, delay_huruf in lirik:
        for c in teks:
            print(c, end='', flush=True)
            time.sleep(delay_huruf)
        print()
        time.sleep(delay_baris)

if __name__ == "__main__":
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.daemon = False  # Ensure thread stops when main program exits
    audio_thread.start()
    print_lirik()
