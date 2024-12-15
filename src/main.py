from googletrans import Translator
from tkinter import *

# Initialize the main window
app_window = Tk()
app_window.title("Language Translator")
app_window.geometry('300x250')
app_window.configure(bg='light cyan')

# Create a Translator instance
translator = Translator()

# Function to perform translation
def translate_text(target_language):
    input_text = text_entry.get()  # Get the input text
    if input_text:  # Check if the input text is not empty
        translated = translator.translate(input_text, dest=target_language).text
        display_translation(translated)
    else:
        display_translation("Please enter text to translate.")

# Function to display the translation on the window
def display_translation(translated_text):
    translation_label.config(text=f'Translation: {translated_text}')

# Create labels and text entry box
label_prompt = Label(app_window, text="Enter text to translate:")
label_prompt.place(x=50, y=10)

text_entry = Entry(app_window, width=25, font=('Arial', 14), bg="white")
text_entry.place(x=20, y=40)

translation_label = Label(app_window, text="Translation:", font=('Arial Bold', 12), fg='DodgerBlue2')
translation_label.place(x=5, y=220)

# Create buttons for each language translation
button_french = Button(app_window, text='French', padx=8, pady=8, bg="powder blue", width=8, 
                       command=lambda: translate_text('fr'))
button_french.place(x=5, y=75)

button_german = Button(app_window, text='German', padx=8, pady=8, bg="yellow", width=8, 
                       command=lambda: translate_text('de'))
button_german.place(x=90, y=75)

button_spanish = Button(app_window, text='Spanish', padx=8, pady=8, bg="blue", width=8, 
                        command=lambda: translate_text('es'))
button_spanish.place(x=175, y=75)

button_hindi = Button(app_window, text='Hindi', padx=8, pady=8, bg="Green", width=8, 
                      command=lambda: translate_text('hi'))
button_hindi.place(x=5, y=115)

button_turkish = Button(app_window, text='Turkish', padx=8, pady=8, bg="Pink", width=8, 
                        command=lambda: translate_text('tr'))
button_turkish.place(x=90, y=115)

button_chinese = Button(app_window, text='Chinese', padx=8, pady=8, bg="orange", width=8, 
                        command=lambda: translate_text('zh-CN'))
button_chinese.place(x=175, y=115)

button_arabic = Button(app_window, text='Arabic', padx=8, pady=8, bg="white", width=8, 
                       command=lambda: translate_text('ar'))
button_arabic.place(x=5, y=155)

button_persian = Button(app_window, text='Persian', padx=8, pady=8, bg="DodgerBlue2", width=8, 
                        command=lambda: translate_text('fa'))
button_persian.place(x=90, y=155)

# Run the main event loop
app_window.mainloop()
