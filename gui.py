import csv
import os.path
import time
import webbrowser
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from functools import partial
from PIL import Image, ImageTk
from file_operation import FileOperation

def data_csv(filename, operation, execution_time):
    file_path = 'log_operations.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Filename', 'Operation', 'Execution Time'])
        writer.writerow([filename, operation, f"{execution_time} seconds"])

def browse_files():
    browse_files.filename = filedialog.askopenfilename(initialdir="/", title="Select a File")
    if not browse_files.filename:
        messagebox.showerror("Error", "No file selected. Please select a file.")
        return
    file_label.configure(text="File Opened: " + browse_files.filename)

def encrypt_file(entered_key):
    try:
        if browse_files.filename is None:
            messagebox.showerror("Error", "No file selected. Please select a file.")
            return

        temp_key = entered_key.get()
        if not temp_key:
            messagebox.showerror("Error", "Please enter an encryption key.")
            return

        temp_key = ''.join(e for e in temp_key if e.isalnum())
        key = temp_key + ("s" * (43 - len(temp_key)) + "=")
        fernet = Fernet(key)

        start_time = time.time()

        with open(browse_files.filename, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(browse_files.filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        end_time = time.time()
        execution_time = round(end_time - start_time, 4)

        file_operation = FileOperation(browse_files.filename, 0, execution_time)
        print(file_operation)

        data_csv(browse_files.filename, "0", execution_time)

        status_label.configure(text="You have successfully encrypted the file.", fg="black", bg="white")

    except Exception as e:
        messagebox.showerror("Error", "Incorrect key entered. Try again.")


def decrypt_file():
    try:
        if browse_files.filename is None:
            messagebox.showerror("Error", "No file selected. Please select a file.")
            return

        temp_key = entered_password.get()
        if not temp_key:
            messagebox.showerror("Error", "Please enter a decryption key.")
            return

        temp_key = ''.join(e for e in temp_key if e.isalnum())
        key = temp_key + ("s" * (43 - len(temp_key)) + "=")
        fernet = Fernet(key)

        start_time = time.time()

        with open(browse_files.filename, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(browse_files.filename, 'wb') as dec_file:
            dec_file.write(decrypted)

        end_time = time.time()
        execution_time = round(end_time - start_time, 4)

        file_operation = FileOperation(browse_files.filename, 1, execution_time)
        print(file_operation)

        data_csv(browse_files.filename, "1", execution_time)

        status_label.configure(text="You have successfully decrypted the file.", fg="black", bg="white")

    except Exception as e:
        messagebox.showerror("Error", "Incorrect key entered. Try again.")

def send_email():
    recipient_email = ""
    subject = ""
    body = ""
    webbrowser.open_new("mailto:{}?subject={}&body={}".format(recipient_email, subject, body))

def toggle_password():
    if password.cget('show') == '':
        password.config(show='*')
    else:
        password.config(show='')

window = Tk()
window.title('Microsoft CryptoVault')
window.geometry("900x740")
window.config(background="white")

main_title = Label(window, text="Encryption and Decryption Tool", fg="black", bg="white", font=("", 30))
main_title.pack(pady=(70, 10))

image = Image.open("microsoft-tower.png")
image = image.resize((300, 300), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = Label(window, image=photo, bg="white")
image_label.pack(pady=(20, 20))

file_button = Button(window, text="Browse File", command=browse_files, width=25, height=2, font=("Roboto", 30))
file_button.pack()

file_label = Label(window, text="File Opened : ", fg="black", bg="white", font=("Roboto", 15))
file_label.pack()

password_label = Label(window, text="Enter Key : ", fg="black", bg="white", font=("Roboto", 15))
password_label.pack()

entered_password = StringVar()
password = Entry(window, textvariable=entered_password, show="*")
password.pack()

check_show_password = Checkbutton(window, text="Show Password", command=toggle_password, fg="black", bg="white", font=("Roboto", 12))
check_show_password.pack()

encrypt_button = Button(window, text="Encrypt", command=partial(encrypt_file, entered_password), width=25, height=2, font=("Roboto", 15))
encrypt_button.pack()

decrypt_button = Button(window, text="Decrypt", command=decrypt_file, width=25, height=2, font=("Roboto", 15))
decrypt_button.pack()

send_email_button = Button(window, text="Send Email", command=send_email, width=25, height=2, font=("Roboto", 15))
send_email_button.pack()

exit_button = Button(window, text="Exit", command=window.quit, width=25, height=2, font=("Roboto", 15))
exit_button.pack()

status_label = Label(window, text="", fg="black", bg="white", font=("Roboto", 14))
status_label.pack()

window.mainloop()
