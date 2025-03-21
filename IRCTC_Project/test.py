# from rembg import remove
# from PIL import Image
# input_path = "roko.png"
# output_path = "output.png"
#
# img = Image.open(input_path)
# output = remove(img)
# output.save(output_path)
#
# print("background removed successfully")
#
# from rembg import remove
# from PIL import Image
#
# # Define input and output file paths
# input_path = "rok0.png"
# output_path = "output.png"
#
# try:
#     # Open the image
#     with Image.open(input_path) as img:
#         # Remove the background
#         output = remove(img)
#
#         # Save the processed image
#         output.save(output_path)
#
#     print("Background removed successfully.")
#
# except FileNotFoundError:
#     print(f"Error: The file '{input_path}' was not found.")
#
# except Exception as e:
#     print(f"An error occurred: {e}")



import os
from rembg import remove
from PIL import Image

input_path = "rok0.png"  # Change to full path if needed
output_path = "output.png"

# Check if file exists before processing
if not os.path.exists(input_path):
    print(f"Error: File '{input_path}' not found. Please check the file path.")
else:
    try:
        with Image.open(input_path) as img:
            output = remove(img)
            output.save(output_path)
        print("Background removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
