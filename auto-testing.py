from file_operation import FileOperation
from tkinter import messagebox

class TestFileOperation:
    def test_encryption(self):
        print("Test Case 1: can create a new FileOperation instance for Encryption ")
        execution_time = None
        file1 = FileOperation('/Users/jessicalongstreth/chanelbleu.jpg', 0, execution_time)
        assert('/Users/jessicalongstreth/chanelbleu.jpg', 0, execution_time) == \
              (file1.filename, file1.operation, file1.execution_time)

    def test_decryption(self):
        print("Test Case 2: can create a new FileOperation instance for Decryption ")
        execution_time = None
        file2 = FileOperation('/Users/jessicalongstreth/bannerlinkedin.png', 1, execution_time)
        assert('/Users/jessicalongstreth/bannerlinkedin.png', 1, execution_time) == \
              (file2.filename, file2.operation, file2.execution_time)

    def test_no_file(self):
        print("Test Case 3: no file entered by user")
        execution_time = None
        file3 = FileOperation('', 0, execution_time)
        if not file3.filename:
            messagebox.showerror("Error", "No file selected. Please select a file.")
        assert ('', 0, execution_time) == \
               (file3.filename, file3.operation, file3.execution_time)


