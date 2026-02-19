import os
import shutil

path = "C:/Users/MOHIT/Downloads"

image_extensions = {".jpg", ".png", ".jpeg"}
pdf_extensions = {".pdf"}
video_extensions = {".mp4", ".mkv"}

files = os.listdir(path)

for file in files:
    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):

        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in image_extensions:
            folder_name = "Images"
        elif ext in pdf_extensions:
            folder_name = "PDFs"
        elif ext in video_extensions:
            folder_name = "Videos"
        else:
            folder_name = "Others"

        destination_folder = os.path.join(path, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, file)

        shutil.move(full_path, destination_path)

print("Files organized successfully.")
