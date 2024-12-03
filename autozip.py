import os
import zipfile

def zip_folders_in_directory(base_directory):
    # Iterate through all folders in the given base directory
    for foldername, subfolders, filenames in os.walk(base_directory):
        # Skip if there are no files in the folder
        if not filenames:
            continue
        
        # Name of the zip file (same as folder name)
        zip_filename = os.path.join(foldername, os.path.basename(foldername) + ".zip")
        
        # Skip if the zip file already exists
        if os.path.exists(zip_filename):
            print(f"Zip file already exists: {zip_filename}")
            continue
        
        # Create a zip file and add all files in the folder
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                # Add the file to the zip, keeping folder structure relative
                zipf.write(filepath, os.path.relpath(filepath, foldername))
        
        print(f"Zipped folder: {foldername} into {zip_filename}")

# Specify the directory containing the folders
base_directory = input("Enter the path to the base directory: ").strip()

if os.path.isdir(base_directory):
    zip_folders_in_directory(base_directory)
else:
    print("The specified path is not a directory!")
