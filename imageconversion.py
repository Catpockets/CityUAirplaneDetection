from PIL import Image
import os

def resize_images(input_dir, output_dir, new_size=(640, 640)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist

    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg"):  # Process JPEG images
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with Image.open(input_path) as img:
                # Use LANCZOS resampling for high-quality downsampling
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                img.save(output_path)  # Save the resized image

# Define the input and output directories
input_directory = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\images'
output_directory = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\resized_images'

# Call the function
resize_images(input_directory, output_directory)