import os
import zipfile

# Path to the downloaded zip file
zip_file_path = "/mnt/c/Users/adrie/Documents/Projects Data/quantum/customer-churn-dataset.zip"

# Directory to extract the contents
extract_to_dir = "/mnt/c/Users/adrie/Documents/Projects Data/quantum"

# Check if the zip file exists
if os.path.exists(zip_file_path):
    print(f"Found zip file: {zip_file_path}")
    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
        print(f"Extracted contents to: {extract_to_dir}")
else:
    print(f"Zip file does not exist: {zip_file_path}")
