import os
import shutil

# Define file types and their corresponding extensions
FILE_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic", ".raw"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".rtf"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm", ".mpeg", ".mpg", ".m4v"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".aiff", ".alac", ".opus"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".tgz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".sh", ".json", ".xml"],
    "Executables": [".exe", ".bat", ".sh", ".bin", ".app", ".jar", ".out", ".msi", ".apk", ".deb"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".tsv", ".sxc", ".dif", ".dbf", ".slk", ".pxl"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key", ".sxi", ".fodp", ".otp", ".pez", ".gslides", ".prz"],
    "Ebooks": [".epub", ".mobi", ".azw3", ".fb2", ".ibooks", ".lit", ".lrf", ".prc", ".cbr", ".cbz"]
}

def get_file_type(extension):
    """Identify the type category based on file extension."""
    for type_name, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return type_name
    return "Others"  # Uncategorized files

def organize_files(directory):
    """Organize files in the specified directory by file type."""
    # Ensure the path is absolute
    directory = os.path.abspath(directory)

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The path '{directory}' is not a valid directory.")
        return

    # Traverse through files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories and focus only on files
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            file_type = get_file_type(file_extension)

            # Create destination folder if it doesn't exist
            type_folder = os.path.join(directory, file_type)
            os.makedirs(type_folder, exist_ok=True)

            # Move file to the appropriate folder
            shutil.move(file_path, os.path.join(type_folder, filename))
            print(f"Moved: {filename} -> {type_folder}")

    print("\nOrganization Complete!")
    print_directory_structure(directory)

def print_directory_structure(directory, indent_level=0):
    """Print directory structure for visual feedback."""
    items = os.listdir(directory)
    items.sort()
    for item in items:
        item_path = os.path.join(directory, item)
        indent = " " * indent_level
        if os.path.isdir(item_path):
            print(f"{indent}📁 {item}")
            print_directory_structure(item_path, indent_level + 4)
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    target_dir = input("Enter the directory to organize: ").strip()
    organize_files(target_dir)