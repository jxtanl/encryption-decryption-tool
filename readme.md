# Final Project (Jessica Longstreth)

CryptoVault is a file encryption/decryption application, envisioned to seamlessly
integrate with existing productivity services utilized across Microsoft's
App Developers, IT Administrators, Management, and Employees. Users 
will be able to browse, select, encrypt, and decrypt a file. Application also allows
users to directly email their encrypted file from the user interface 
and cleanly exit the program. 

## Install required libraries
Ensure that you are in the main directory and 
run the following:

_This must be done before you can run the application
if you are not using the included venv._

```shell
$ pip install cryptography
$ pip install PILLOW
$ pip install pytest
```

## To run the program
Click the green triangle run icon in the 
top-right corner of the PyCharm window.
or
```shell
$ python3 gui.py
```

## Functionality
### Browse File
Users can navigate their file systems on Windows, macOS, 
and Linux. Upon selecting file, it will be added to the list 
of instances within the FileOperation Class and logged into 
the log_operations.csv file. All file types are accepted.

When clicking the Browse File button, the browse_files function
will be called to create a new FileOperation instance. 

When printing out the FileOperation Class instance list, the
following information will be displayed:

Filename: /Users/jessicalongstreth/chanelbleu.jpg 
Operation: 0
Time Taken: 0.0676 seconds

### Encrypt Selected File

Users can encrypt their selected file using symmetric 
encryption algorithm provided by the cryptography library.
After selecting a file, users enter an encryption key. 
The selected file will then be encrypted using the provided 
key and saved back to its original location. This functionality 
ensures security and confidentiality by making the file inaccessible 
without the correct decryption key. The operation type and 
execution time are logged in the log_operations.csv file 
when the Encrypt button is clicked.

### Decrypt Selected File

Users can decrypt their selected file using symmetric decryption 
algorith provided by the cryptography library. After selecting 
the encrypted file, users are prompted to enter the decryption key. 
Upon providing the correct key, the selected file is decrypted and
restored to its original format, making the contents accessible
again. This functionality ensures users can securely access and 
recover their encrypted data as needed. Likewise, the operation 
type and execution time are logged in the log_operations.csv file
when the Decrypt button is clicked. 

### Email Selected File

Users can share a selected file via email directly from the 
application. After selecting a file, users initiate the email 
sending process by clicking the Send Email button. This action
opens the default email browser and users can specify the recipient
email address, subject, and body of the email before sending it. 
This functionality eliminated the need to open a separate email
application, making the user's experience effortless and efficient.

### Exit

The application will close when the Exit button is clicked.

## Data file
### log_operations.csv
The file contains the transaction data in the 
following format:

| Filename                                  | Operation | Execution Time    |
|-------------------------------------------|-----------|-------------------|
| /Users/jessicalongstreth/chanelbleu.jpg   | 0         |  0.0676 seconds   |
| /Users/jessicalongstreth/chanelbleu.jpg   | 1         |  0.0051 seconds   |


## Class

### FileOperation Class

#### Variables
The class has one class variable: bank_name

The FileOperation instance has the following instance
variables:
1. filename: private, string data type
2. operation: private, integer data type
3. execution_time: private, float data type

#### Methods
The FileOperation class has the following methods:
* The __init__ method
* The __str__ method


## Auto Testing
Run the following command to test the 
auto-testing.py file.  There are 3 test cases.

```shell
$ pytest -v auto-testing.py
```