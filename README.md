# AI Image Prompt Extractor

## Overview

This script extracts and prints the prompt and metadata (Exif and other metadata) from an image file using the Python Imaging Library (PIL). Metadata in images can contain a variety of information such as camera settings, GPS location, and other details.

## Requirements

Python 3.x

PIL (Pillow)

OS module

string module

## Installation

Install Python from python.org.

Install Pillow by running the following command:

    pip install pillow

## Usage

Replace the image_path variable in the script with the path to your image file.

Run the script using Python.

    python AI_Image_Prompt_Extractor.py

## Script Parameters

image_path: The path to the image file from which metadata will be extracted.

## Example Usage

To use this script, replace the example path with your actual image file path:

    if __name__ == "__main__":
        image_path = r"C:\Users\User\Desktop\Example.jpg"  # Replace with the path to your image
        extract_metadata(image_path)

## Modifying Parameters
### How to Change Parameters

To change the image file for prompt and metadata extraction, modify the image_path variable:

    if __name__ == "__main__":
        image_path = r"C:\path\to\your\image.jpg"  # Replace with the path to your image
        extract_metadata(image_path)

## Effects of Parameters

Changing the image_path parameter will change the image from which metadata is extracted. The script will print the prompt, Exif metadata and other available metadata of the specified image.

## Example Output

After running the script, the console will display the extracted prompt and metadata in the following format:

    Exif Metadata:
    ImageWidth: 4000
    ImageLength: 3000
    Make: Canon
    Model: Canon EOS 80D
    ...

    Other Metadata:
    dpi: (72, 72)

If no Exif metadata is found, the script will print:

    No Exif metadata found.

## Error Handling

The script includes basic error handling to catch and display any errors that occur during execution. If an error occurs, it will be printed to the console.

## License

This script is provided under the MIT License. Feel free to use and modify it as needed.

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue on the GitHub repository.
