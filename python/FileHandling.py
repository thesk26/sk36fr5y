# Day 19 
# 10/06/2025
# class 19

# File Handling in Python
# File handling is a crucial aspect of programming that allows you to read from and write to files.
# In Python, file handling is done using built-in functions and methods that allow you to open, read, write, and close files.       
# Opening a file
file = open('example.txt', 'w')  # 'w' mode opens the file for writing (creates it if it doesn't exist)
# Writing to a file
file.write('Hello, World!\n')
# Closing a file
file.close()
# Reading from a file
file = open('example.txt', 'r')  # 'r' mode opens the file for reading
content = file.read()  # Read the entire content of the file
print(content)  # Output: Hello, World!
# Closing the file after reading
file.close()
# Using 'with' statement for file handling
with open('example.txt', 'a') as file:  # 'a' mode opens the file for appending
    file.write('Appending a new line.\n')  # Appending a new line to the file
# Reading the file again to see the appended content
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nAppending a new line.
# Working with file paths
import os
# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")
# Joining paths
file_path = os.path.join(current_directory, 'example.txt')
print(f"File Path: {file_path}")
# Checking if a file exists
if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
# Deleting a file
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted.")
else:
    print("File does not exist, cannot delete.")
# Creating a new file and writing multiple lines
with open('multi_line.txt', 'w') as file:
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)  # Writing multiple lines to the file
# Reading the multi-line file
with open('multi_line.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Line 1\nLine 2\nLine 3\n
# Appending more lines to the multi-line file
with open('multi_line.txt', 'a') as file:
    file.write("Line 4\n")  # Appending a new line
# Reading the updated multi-line file
with open('multi_line.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Line 1\nLine 2\nLine 3\nLine 4\n
# Reading a file line by line
with open('multi_line.txt', 'r') as file:
    for line in file:  # Iterating through each line in the file
        print(line.strip())  # Output: Line 1\nLine 2\nLine 3\nLine 4\n (without extra newlines)
# Reading a file with a specific encoding       
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)  # Output: Hello, World!\nAppending a new line.
# Handling file exceptions
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
# Writing binary data to a file
with open('binary_file.bin', 'wb') as file:  # 'wb' mode opens the file for writing in binary mode
    file.write(b'\x00\x01\x02\x03\x04')  # Writing binary data
# Reading binary data from a file
with open('binary_file.bin', 'rb') as file:  # 'rb' mode opens the file for reading in binary mode
    binary_content = file.read()  # Reading the binary content
    print(binary_content)  # Output: b'\x00\x01\x02\x03\x04'
# Working with CSV files
import csv
# Writing to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])  # Writing header
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
# Reading from a CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # Output: ['Name', 'Age', 'City'], ['Alice', '30', 'New York'], ['Bob', '25', 'Los Angeles']
# Working with JSON files
import json
# Writing to a JSON file
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)  # Writing JSON data with indentation
# Reading from a JSON file
with open('data.json', 'r') as jsonfile:
    data = json.load(jsonfile)  # Loading JSON data
    print(data)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Working with XML files
import xml.etree.ElementTree as ET
# Writing to an XML file
root = ET.Element("data")
child1 = ET.SubElement(root, "person")
child1.set("name", "Alice")
child1.set("age", "30")
child1.set("city", "New York")
child2 = ET.SubElement(root, "person")
child2.set("name", "Bob")
child2.set("age", "25")
child2.set("city", "Los Angeles")
tree = ET.ElementTree(root)
tree.write("data.xml")  # Writing XML data to a file
# Reading from an XML file
tree = ET.parse('data.xml')  # Parsing the XML file
root = tree.getroot()  # Getting the root element
for person in root.findall('person'):
    name = person.get('name')
    age = person.get('age')
    city = person.get('city')
    print(f"Name: {name}, Age: {age}, City: {city}")  # Output: Name: Alice, Age: 30, City: New York
# Name: Bob, Age: 25, City: Los Angeles
# Working with file permissions
import stat
# Changing file permissions
def change_file_permissions(file_path, mode):
    os.chmod(file_path, mode)  # Changing the file permissions
    print(f"Permissions for {file_path} changed to {oct(mode)}")
# Example usage
change_file_permissions('example.txt', stat.S_IRUSR | stat.S_IWUSR)  # Read and write permissions for the owner
# Checking file permissions
def check_file_permissions(file_path):
    permissions = stat.filemode(os.stat(file_path).st_mode)  # Getting the file permissions
    print(f"Permissions for {file_path}: {permissions}")
# Example usage
check_file_permissions('example.txt')  # Checking the permissions of the file
# Working with temporary files
import tempfile
# Creating a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'This is a temporary file.\n')  # Writing to the temporary file
    temp_file_path = temp_file.name  # Getting the path of the temporary file
print(f"Temporary file created at: {temp_file_path}")
# Reading from the temporary file
with open(temp_file_path, 'r') as file:
    content = file.read()  # Reading the content of the temporary file
    print(content)  # Output: This is a temporary file.
# Deleting the temporary file
os.remove(temp_file_path)  # Deleting the temporary file
# Confirming deletion
if not os.path.exists(temp_file_path):
    print("Temporary file deleted successfully.")
else:
    print("Temporary file still exists.")
# Working with file locks
import fcntl
# Locking a file
def lock_file(file_path):
    with open(file_path, 'r+') as file:
        fcntl.flock(file, fcntl.LOCK_EX)  # Locking the file for exclusive access
        print(f"File {file_path} is locked.")
        # Perform file operations here
        fcntl.flock(file, fcntl.LOCK_UN)  # Unlocking the file
        print(f"File {file_path} is unlocked.")
# Example usage
lock_file('example.txt')  # Locking the example file
# Working with file encodings
def write_file_with_encoding(file_path, content, encoding='utf-8'):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)  # Writing content with specified encoding
# Example usage
write_file_with_encoding('encoded_file.txt', 'Hello, World!', encoding='utf-8')  # Writing with UTF-8 encoding
# Reading a file with a specific encoding
def read_file_with_encoding(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()  # Reading content with specified encoding
        return content
# Example usage
content = read_file_with_encoding('encoded_file.txt', encoding='utf-8')  # Reading with UTF-8 encoding
print(content)  # Output: Hello, World!
# Working with file metadata
import os
def get_file_metadata(file_path):
    metadata = os.stat(file_path)  # Getting file metadata
    print(f"File: {file_path}")
    print(f"Size: {metadata.st_size} bytes")
    print(f"Last modified: {metadata.st_mtime}")
    print(f"Creation time: {metadata.st_ctime}")
    print(f"Permissions: {oct(metadata.st_mode)}")
# Example usage
get_file_metadata('example.txt')  # Getting metadata for the example file
# Working with file compression
import zipfile
def compress_files(file_paths, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for file in file_paths:
            zipf.write(file)  # Adding files to the zip archive
    print(f"Files compressed into {zip_file_name}")
# Example usage
compress_files(['example.txt', 'multi_line.txt'], 'compressed_files.zip')  # Compressing files into a zip archive
# Extracting files from a zip archive
def extract_files(zip_file_name, extract_to):
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zipf.extractall(extract_to)  # Extracting all files to the specified directory
    print(f"Files extracted to {extract_to}")
# Example usage
extract_files('compressed_files.zip', 'extracted_files')  # Extracting files from the zip archive
# Confirming extraction
import os
extracted_files_path = 'extracted_files'
if os.path.exists(extracted_files_path):
    print(f"Files extracted successfully to {extracted_files_path}.")
else:
    print("Extraction failed, directory does not exist.")
# Working with file globbing
import glob
def list_files_with_pattern(pattern):
    files = glob.glob(pattern)  # Listing files matching the specified pattern
    print(f"Files matching pattern '{pattern}':")
    for file in files:
        print(file)  # Output: List of files matching the pattern
# Example usage
list_files_with_pattern('*.txt')  # Listing all text files in the current directory
# Working with file timestamps
import time
def get_file_timestamp(file_path):
    timestamp = os.path.getmtime(file_path)  # Getting the last modified time of the file
    print(f"Last modified time for {file_path}: {time.ctime(timestamp)}")  # Converting timestamp to human-readable format
# Example usage     
get_file_timestamp('example.txt')  # Getting the last modified time for the example file
# Working with file system operations
import shutil
def copy_file(src, dst):
    shutil.copy(src, dst)  # Copying a file from source to destination
    print(f"File copied from {src} to {dst}")
# Example usage
copy_file('example.txt', 'example_copy.txt')  # Copying the example file
# Moving a file
def move_file(src, dst):
    shutil.move(src, dst)  # Moving a file from source to destination
    print(f"File moved from {src} to {dst}")
# Example usage
move_file('example_copy.txt', 'moved_example.txt')  # Moving the copied file
# Deleting a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  # Deleting the specified file
        print(f"File {file_path} deleted.")
    else:
        print(f"File {file_path} does not exist, cannot delete.")

######################

# create a text file

with open("demo.txt", "w") as f:
    f.write("Hello World! This is a test.")    #optional

# wring a file 
# repalce all the data i the file

#  1code

f = open("demo1.txt" , "w")
f = open("demo1.txt" , "a")                # append the data add it to the file
f.write("i want to learn a python as well as a javascript from tommorow")
f.write("\n then i will move to the react.js")      # append the data add it to the file 
f.close()

# readfile

f = open("demo1.txt", "r")
data = f.read(15)    # Read only first 9 characters from the file
print(data)
print(type(data))
f.close()          #  close a file

# line by line read a data line1 function have \n space whih is recognised by line 1 so there is space 

f = open("demo1.txt" , "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

f = open("demo.txt", "r")
for x in f:
    print(x)

# reading and writing

f = open("demo.txt", "r+")   # this is show i text file
f.write("This")
print(f.read())
f.close()         

# with  syntax
# read data by using with ther is no need to close fiel it auto cloases it

with open("demo1.txt", "r") as f:
    data = f.read()
    print(data) 

with open("demo.txt", "w") as f:
        f.write("new data")
        f.write("\n new data")

with open("demo.txt", "w") as file:
    file.write("\nHello, World!")
    print ("Content added Successfully!!")

file = open("demo.txt", "w")
file.write("This is an example.\n")
file.close()
print ("File closed successfully!!")

file = open("demo.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")

# READ files

# Open the file in read mode
file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

f = open("demo.txt", "w")  
f.write("Woops! I have deleted the content!")  
f.close()

# open and read the file after writing
f = open("demo.txt", "r")  
print(f.read())

# Step 1: Create and write to a text file

with open("demo3.txt", "w") as f:
    f.write("Python is awesome\n")
    f.write("File handling is powerful\n")
    f.write("We are learning split function\n")

# Step 2: Read and split lines

with open("demo3.txt", "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()  # split by default on spaces
        print(words)

# Step 3: Create a new file and write the split words
with open("split_words.txt", "w") as new_file:
    for line in data:
        words = line.split()
        for word in words:
            new_file.write(word + "\n")  # write each word on a new line

# Step 4: Read the new file to verify

# try:
try:
    f = open("myfile2.txt", "x")
    print("File created!")
except FileExistsError:
    print("File already exists!")

f = open("myfile.txt", "w")
f.write("ashwini")

# in short
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# DElete the filed .txt
import os

# Remove a file
os.remove("demo3.txt")
