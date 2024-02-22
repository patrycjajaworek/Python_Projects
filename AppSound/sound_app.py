import os
from tkinter import *
from tkinter import filedialog
from pydub.generators import WhiteNoise
from gtts import gTTS
import pygame
#import speech_recognition as sr
from pydub import AudioSegment
from difflib import get_close_matches

created_files = []
pygame.mixer.init()


def adjust_snr(input_filename, output_filename, snr_level):
    sound = AudioSegment.from_file(input_filename)

    # Adjust the volume of the sound to achieve the desired SNR
    sound = sound - sound.dBFS + snr_level

    # Export the result
    sound.export(output_filename, format="mp3")


def process_sounds_with_snr(input_folder, output_folder, snr_levels):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            input_path = os.path.join(input_folder, filename)

            for snr_level in snr_levels:
                snr_folder = f"{snr_level}dB"
                os.makedirs(os.path.join(output_folder, snr_folder), exist_ok=True)
                output_filename = os.path.join(output_folder, snr_folder, filename)
                adjust_snr(input_path, output_filename, snr_level)


def convert_mp3_to_wav(mp3_filename):
    sound = AudioSegment.from_mp3(mp3_filename)
    wav_filename = mp3_filename.replace(".mp3", ".wav")
    sound.export(wav_filename, format="wav")
    return wav_filename

def play_text_to_speech():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    message = entry_field.get()
    cleaned_message = message.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(":", "_").replace("*",                                                                                                      "_").replace(
        "?", "_").replace("\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")
    #speech = gTTS(text=message)
    speech = gTTS(text=message, lang='pl')  # wersja po polsku

    sounds_folder = "sounds"
    os.makedirs(sounds_folder, exist_ok=True)

    #filename = f"{cleaned_message}.mp3"
    filename = os.path.join(sounds_folder, f"{cleaned_message}.mp3")

    speech.save(filename)
    created_files.append(filename)

    process_sounds_with_snr(sounds_folder, os.path.join(sounds_folder, "snr"), [-10,-5,0,5, 10,15,20,30])

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    pygame.mixer.init()



def compare_texts(user_input):
    reference_text = reference_entry.get()

    if compare_texts_flexible(user_input, reference_text):
        result_label.config(text="Match! Both texts are the same.", fg="green")
    else:
        result_label.config(text="No match! Texts are different.", fg="red")

def compare_texts_flexible(user_input, reference_text):
    user_input_lower = user_input.lower()
    reference_text_lower = reference_text.lower()

    user_words = user_input_lower.split()
    reference_words = reference_text_lower.split()

    for user_word in user_words:

        if user_word not in reference_words:
            close_matches = get_close_matches(user_word, reference_words)
            if not close_matches:
                return False

    return True

def exit_app():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    # for file in created_files:
    #     os.remove(file)

    root.destroy()

def reset_entry():
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    entry_field.delete(0, 'end')
    reference_entry.delete(0, 'end')





root = Tk()
root.geometry("500x400")
root.configure(bg='lightblue')
root.title("Text to Speech Converter")

# Okno do wprowadzania tekstu do odczytania
frame1 = Frame(root, bg='lightblue')
frame1.pack(pady=10)

Label(frame1, text="Enter Text", font='arial 15 bold', bg='lightblue').grid(row=0, column=0)

entry_field = Entry(frame1, width=40)
entry_field.grid(row=0, column=1, pady=10)

play_button = Button(frame1, text="Play", font='arial 15 bold', command=play_text_to_speech)
play_button.grid(row=1, column=0, columnspan=2, pady=10)

# Okno do wprowadzania tekstu do porównania
frame2 = Frame(root, bg='lightblue')
frame2.pack(pady=10)

Label(frame2, text="Enter Reference Text", font='arial 15 bold', bg='lightblue').grid(row=0, column=0)

reference_entry = Entry(frame2, width=40)
reference_entry.grid(row=0, column=1, pady=10)

#record_button = Button(frame2, text="Record", font='arial 15 bold', command=compare_texts)
record_button = Button(frame2, text="Record", font='arial 15 bold', command=lambda: compare_texts(entry_field.get()))

record_button.grid(row=1, column=0, columnspan=2, pady=10)


result_label = Label(root, text="", font='arial 15 bold', bg='lightblue')
result_label.pack(pady=10)

exit_button = Button(root, text='Exit', font='arial 15 bold', command=exit_app, bg='OrangeRed1')
exit_button.pack(pady=10)

reset_button = Button(root, text='Reset', font='arial 15 bold', command=reset_entry)
reset_button.pack(pady=10)



root.mainloop()