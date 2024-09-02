import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pdf2image import convert_from_path

def convert_file(input_path, output_path_png, output_path_jpg, dpi=400):
    file_extension = os.path.splitext(input_path)[1].lower()
    
    if file_extension == '.png':
        with Image.open(input_path) as img:
            img.save(output_path_png, 'PNG')
            rgb_img = img.convert('RGB')
            rgb_img.save(output_path_jpg, 'JPEG', quality=95, dpi=(dpi, dpi))
    elif file_extension == '.pdf':
        pages = convert_from_path(input_path, dpi=dpi)
        if len(pages) == 1:
            pages[0].save(output_path_png, 'PNG')
            pages[0].convert('RGB').save(output_path_jpg, 'JPEG', quality=95)
        else:
            for i, page in enumerate(pages):
                page.save(f"{output_path_png[:-4]}_{i+1}.png", 'PNG')
                page.convert('RGB').save(f"{output_path_jpg[:-4]}_{i+1}.jpg", 'JPEG', quality=95)
    else:
        print(f"Unsupported file format: {file_extension}")

def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select PNG and PDF files", 
                                             filetypes=[("PNG and PDF files", "*.png *.pdf")])
    return file_paths

def ask_rewrite():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    response = messagebox.askyesno("File Handling", "Do you want to rewrite existing converted files?")
    return response

def main():
    input_files = select_files()
    if not input_files:
        print("No files selected. Exiting.")
        return

    # Check if there are any existing converted files
    existing_files = [f for f in input_files if os.path.exists(f[:-4] + '.png') or os.path.exists(f[:-4] + '.jpg')]
    rewrite = False
    if existing_files:
        rewrite = ask_rewrite()

    for input_path in input_files:
        output_path_png = os.path.splitext(input_path)[0] + '.png'
        output_path_jpg = os.path.splitext(input_path)[0] + '.jpg'
        
        # Check if the output files already exist
        if (os.path.exists(output_path_png) or os.path.exists(output_path_jpg)) and not rewrite:
            print(f"Skipping {os.path.basename(input_path)} - converted file(s) already exist")
            continue
        
        convert_file(input_path, output_path_png, output_path_jpg)
        print(f"Converted {os.path.basename(input_path)} to PNG and JPEG")

    print("All conversions complete.")

if __name__ == "__main__":
    main()