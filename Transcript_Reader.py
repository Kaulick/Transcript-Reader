import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import pyperclip
import PyPDF2

class Navigator:
    def __init__(self, master):
        self.master = master
        self.master.title("Navigator")
        self.master.geometry("300x200")

        self.label = tk.Label(master, text="Navigator is On", font=("Arial", 16))
        self.label.pack(pady=20)

        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.read_button = tk.Button(master, text="Read Selected Text", command=self.read_text)
        self.read_button.pack(pady=10)

        self.engine = pyttsx3.init()
        self.file_path = None
        self.file_text = ""

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
        if file_path:
            self.file_path = file_path
            self.file_text = self.extract_text_from_file(file_path)
            if self.file_text:
                messagebox.showinfo("File Selected", f"Selected file: {file_path}")
            else:
                messagebox.showwarning("No Text Found", "The selected file does not contain readable text.")
        else:
            messagebox.showwarning("No File Selected", "Please select a file.")

    def extract_text_from_file(self, file_path):
        if file_path.endswith('.pdf'):
            return self.extract_text_from_pdf(file_path)
        elif file_path.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        return ""

    def extract_text_from_pdf(self, file_path):
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()

    def read_text(self):
        if self.file_text:
            self.engine.say(self.file_text)
            self.engine.runAndWait()
        else:
            messagebox.showwarning("No Text Found", "Please select a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    navigator = Navigator(root)
    root.mainloop()