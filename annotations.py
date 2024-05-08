import os
from PIL import Image

def convert_bbox(image_dir, bbox_file, output_dir, default_class_id=0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create output directory if it doesn't exist
    
    with open(bbox_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:  # Check if line format is correct
                image_id, xmin, ymin, xmax, ymax = parts
                xmin, ymin, xmax, ymax = map(int, [xmin, ymin, xmax, ymax])
                # Calculate YOLO format values
                with Image.open(os.path.join(image_dir, f"{image_id}.jpg")) as img:
                    x_center = (xmin + xmax) / 2.0 / img.width
                    y_center = (ymin + ymax) / 2.0 / img.height
                    width = (xmax - xmin) / img.width
                    height = (ymax - ymin) / img.height

                # Save to corresponding annotation file
                annotation_path = os.path.join(output_dir, f"{image_id}.txt")
                with open(annotation_path, 'a') as ann_file:
                    ann_file.write(f"{default_class_id} {x_center} {y_center} {width} {height}\n")

# Define paths
image_directory = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\resized_images'
bbox_file_path = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\images_box.txt'
annotations_output_directory = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\labels'

# Convert bounding boxes
convert_bbox(image_directory, bbox_file_path, annotations_output_directory)