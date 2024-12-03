import os

def write_direct_subfolder_paths(parent_folder):
    try:
        # Remove surrounding quotes if present
        parent_folder = parent_folder.strip('"')

        # Extract the folder name to use for the output file name
        folder_name = os.path.basename(parent_folder.rstrip("\\/"))
        output_file = os.path.join(parent_folder, f"{folder_name}.txt")

        # Get only the direct subfolders within the parent folder
        subfolders = [
            os.path.join(parent_folder, folder) 
            for folder in os.listdir(parent_folder) 
            if os.path.isdir(os.path.join(parent_folder, folder))
        ]

        # Sort the subfolders alphabetically
        subfolders.sort()

        # Write the paths in the specified format to the output file
        with open(output_file, 'w') as file:
            for folder in subfolders:
                file.write(f'"{folder}" | False\n')

        print(f'Formatted folder paths from "{parent_folder}" have been written to "{output_file}".')
    except Exception as e:
        print(f"An error occurred: {e}")

# Take user input for the folder path
parent_folder = input('Enter the folder path (e.g., "D:\\YourFolder"): ').strip()

# Call the function
write_direct_subfolder_paths(parent_folder)
