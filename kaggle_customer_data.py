import os
import subprocess

# Set target directory
download_dir = "/mnt/c/Users/adrie/Documents/Projects Data/quantum"
print(f"Download directory: {download_dir}")

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

# Download the dataset using Kaggle CLI
kaggle_command = [
    "kaggle", "datasets", "download", "-d", "muhammadshahidazeem/customer-churn-dataset",
    "-p", download_dir
]
subprocess.run(kaggle_command, check=True)
print(f"Dataset downloaded to: {download_dir}")

