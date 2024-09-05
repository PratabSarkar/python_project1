import tkinter as tk
from tkinter import ttk, messagebox
from translate import Translator
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        # Get the selected language names
        source_lang_name = source_lang_combobox.get()
        target_lang_name = target_lang_combobox.get()

        # Convert language names to codes
        source_lang_code = [code for code, name in LANGUAGES.items() if name == source_lang_name][0]
        target_lang_code = [code for code, name in LANGUAGES.items() if name == target_lang_name][0]

        # Get the text to translate
        text_to_translate = source_text.get("1.0", tk.END).strip()
        
        if not text_to_translate:
            messagebox.showwarning("Warning", "Please enter text to translate")
            return
        
        # Initialize the translator
        translator = Translator()

        # Perform translation
        translated = translator.translate(text_to_translate, src=source_lang_code, dest=target_lang_code)

        # Update the target text field with the translated text
        target_text.delete("1.0", tk.END)
        target_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

def clear_text():
    source_text.delete("1.0", tk.END)
    target_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Window size
root.geometry("500x400")

# Source language
source_lang_label = tk.Label(root, text="Source Language")
source_lang_label.pack(pady=5)

source_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
source_lang_combobox.pack(pady=5)
source_lang_combobox.set("english")  # default value

# Target language
target_lang_label = tk.Label(root, text="Target Language")
target_lang_label.pack(pady=5)

target_lang_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
target_lang_combobox.pack(pady=5)
target_lang_combobox.set("french")  # default value

# Source text
source_text_label = tk.Label(root, text="Enter text")
source_text_label.pack(pady=5)

source_text = tk.Text(root, height=5, width=50)
source_text.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Target text
target_text_label = tk.Label(root, text="Translated text")
target_text_label.pack(pady=5)

target_text = tk.Text(root, height=5, width=50)
target_text.pack(pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=10)

# Run the application
root.mainloop()


