# Transcript-Reader

This Python-based application, Transcript Reader, allows users to select files (PDF or TXT), extract text, and convert the text to speech using a user-friendly graphical interface.

Features

File Selection: Choose text or PDF files using a dialog box.
Text Extraction: Extract text content from the selected file.
Text-to-Speech: Read the extracted text aloud using pyttsx3.
Error Handling: Alerts users if no file is selected or no text is found.
Prerequisites

Before running the application, ensure you have the following libraries installed:

tkinter (comes pre-installed with Python)
pyttsx3
pyperclip
PyPDF2

Install additional dependencies using:

pip install pyttsx3 pyperclip PyPDF2  

How to Use

Clone the repository or download the script.
Run the script:

python navigator.py 

Use the graphical interface to:
Select a file (TXT or PDF).
Extract and read text from the file.
.
├── navigator.py  # Main script
└── README.md     # Documentation

Notes
Ensure the selected PDF contains readable text; scanned PDFs or images won't work.
Text-to-speech functionality depends on the pyttsx3 library configuration.


Contributions
Feel free to open issues or submit pull requests for improvements and feature enhancements.

Enjoy using Transcript Reader! 🚀
