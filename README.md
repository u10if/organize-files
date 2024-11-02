
# File Organizer Script

A simple Python script to automatically organize files in a specified directory by type. It classifies files into categories (like images, documents, videos, etc.), moves them into type-specific folders, and provides a structured overview after organization. This project is intended for quick cleanup and organization of folders on a Mac.

## Features

- **Automatic Classification**: Recognizes 10 file types by default, including images, documents, videos, and archives.
- **Customizable**: Easily expand or modify the file type categories and extensions.
- **Simple Directory Structure Display**: Shows the organized directory structure after processing.
- **Cross-Platform Compatibility**: Designed for Mac but works on Linux and Windows with minimal adjustments.

## File Types Supported

The script classifies files into the following categories:

1. Images
2. Documents
3. Videos
4. Music
5. Archives
6. Code
7. Executables
8. Spreadsheets
9. Presentations
10. Ebooks

Each category has a predefined set of file extensions (e.g., `.jpg`, `.pdf`, `.mp4`). Files not fitting these categories are placed in an "Others" folder.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script:
    ```bash
    git clone https://github.com/u10if/organize-files.git
    cd organize-files
    ```

2. Run the script:
    ```bash
    python3 organize.py
    ```

## Usage

1. **Run the Script**: Launch the script and provide the directory you want to organize when prompted.
2. **Directory Structure**: The script creates folders for each file type (if files of that type exist) and moves the files accordingly.
3. **View Results**: After organizing, the script will print the updated directory structure for easy reference.

Example usage:
```bash
python3 organize.py
Enter the directory to organize: /path/to/your/directory

Example Directory Structure

After running the script, you might see a structure like this:

/path/to/your/directory
│
├── Images
│   ├── photo1.jpg
│   ├── graphic.png
│
├── Documents
│   ├── report.pdf
│   ├── notes.txt
│
├── Videos
│   ├── movie.mp4
│
└── Others
    ├── randomfile.xyz

Customization

To add or remove file types, update the FILE_TYPES dictionary within file_organizer.py. Each key represents a category, and the list contains associated file extensions.

FILE_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ...],
    "Documents": [".pdf", ".doc", ".txt", ...],
    # Add your custom categories and extensions here
}

Troubleshooting

	1.	Directory Not Found: Ensure the path entered exists. Use absolute paths for reliability.
	2.	Permission Issues: If you encounter permissions errors, ensure the script has permission to modify the files. Run with sudo if necessary:

sudo python3 file_organizer.py



License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Feel free to submit a pull request to enhance the file type categories, improve functionality, or add new features.

Acknowledgments

Inspired by the need for an organized workspace and efficient file management. Special thanks to the open-source community for ideas and guidance on Python scripting.

Note: Always review and back up your files before running any file-organizing scripts.

