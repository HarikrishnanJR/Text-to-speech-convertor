import tkinter as tk
import tkinter.ttk as ttk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create the Tkinter window
window = tk.Tk()
window.title("Text-to-Speech Generator")

# Create the style for the window
style = ttk.Style(window)
style.configure('TButton', font=('calibri', 12, 'bold'), foreground='blue')

# Create the text input box
text_input = tk.Entry(window, font=('calibri', 16))
text_input.pack(pady=10)

# Create the speak button
def speak_text():
    text = text_input.get()
    engine.say(text)
    engine.runAndWait()

speak_button = ttk.Button(window, text="Speak", command=speak_text)
speak_button.pack(pady=10)

# Create the label and input box for the speech rate
rate_label = ttk.Label(window, text="Speech Rate", font=('calibri', 12))
rate_label.pack(pady=5)

rate_input = ttk.Entry(window, font=('calibri', 12))
rate_input.pack(pady=5)

# Create the label and input box for the speech volume
volume_label = ttk.Label(window, text="Speech Volume", font=('calibri', 12))
volume_label.pack(pady=5)

volume_input = ttk.Entry(window, font=('calibri', 12))
volume_input.pack(pady=5)

# Create the settings button
def apply_settings():
    rate = float(rate_input.get())
    volume = float(volume_input.get())

    # Set the speech rate and volume
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

settings_button = ttk.Button(window, text="Apply Settings", command=apply_settings)
settings_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
