from PIL import Image, ExifTags
import os
import string

TAGS = {v: k for k, v in ExifTags.TAGS.items()}  # Mapping of tag names to their numerical values

def is_printable(s):
    return all(c in string.printable for c in s)

def decode_value(value):
    try:
        decoded_value = value.decode("utf-8", errors="ignore").strip()
        if not is_printable(decoded_value):
            decoded_value = value.decode("latin-1", errors="ignore").strip()
    except UnicodeDecodeError:
        decoded_value = value.decode("latin-1", errors="ignore").strip()
    return decoded_value

def extract_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        print("Exif Metadata:")
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if isinstance(value, bytes):
                    decoded_value = decode_value(value)
                    print(f"{tag_name}: {decoded_value}")
                else:
                    print(f"{tag_name}: {value}")
        else:
            print("No Exif metadata found.")
        
        other_metadata = img.info
        print("\nOther Metadata:")
        for key, value in other_metadata.items():
            if isinstance(value, bytes):
                decoded_value = decode_value(value)
                print(f"{key}: {decoded_value}")
            else:
                print(f"{key}: {value}")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    image_path = r"C:\Users\User\Desktop\Example.jpg"  # Replace with the path to your image
    extract_metadata(image_path)