import cv2
from pyzbar.pyzbar import decode
import csv
import os.path

csv_file = r'C:\Users\User\Desktop\New folder\qr_code_data.csv'

# Check if the CSV file exists
file_exists = os.path.isfile(csv_file)

# Path to the image file
image_path = 'test.jpg'

# Load the image
image = cv2.imread(image_path)

# Decode the QR code
qr_codes = decode(image)

# Initialize a list to hold the QR code data
qr_data_list = []

# Extract QR code data and append to the list
for qr_code in qr_codes:
    data = qr_code.data.decode('utf-8')
    qr_data_list.append(data)

# Write QR code data to the CSV file
with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    # If the file is empty, write the header
    if not file_exists:
        writer.writerow([f'QR Code Data {i+1}' for i in range(len(qr_data_list))])  # Header with column names
    # Transpose the list and write data to columns
    writer.writerow(qr_data_list)

print("QR code data extraction complete.")
