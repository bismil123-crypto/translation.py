import tkinter as tk
from tkinter import filedialog
from googletrans import Translator
from gtts import gTTS
from PIL import Image, ImageTk
import os

# Initialize the translator
translator = Translator()

def translate_text():
    source_text = text_input.get("1.0", tk.END)
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
    translated_text.set(translation.text)

def play_audio():
    text_to_speak = translated_text.get()
    tts = gTTS(text=text_to_speak, lang=dest_lang_var.get())
    audio_file = "translation.mp3"
    tts.save(audio_file)
    os.system(f"start {audio_file}")

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Create the GUI components
text_input = tk.Text(root, height=10, width=50)
text_input.pack(pady=10)

src_lang_var = tk.StringVar(value='auto')
dest_lang_var = tk.StringVar(value='en')

tk.Label(root, text="Source Language Code:").pack()
tk.Entry(root, textvariable=src_lang_var).pack(pady=5)

tk.Label(root, text="Destination Language Code:").pack()
tk.Entry(root, textvariable=dest_lang_var).pack(pady=5)

translated_text = tk.StringVar()
tk.Label(root, text="Translated Text:").pack()
tk.Entry(root, textvariable=translated_text, width=50).pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=5)

audio_button = tk.Button(root, text="Play Audio", command=play_audio)
audio_button.pack(pady=5)

img_button = tk.Button(root, text="Load Image", command=load_image)
img_button.pack(pady=5)

img_label = tk.Label(root)
img_label.pack(pady=10)

# Run the main event loop
root.mainloop()
