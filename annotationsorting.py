import os
import shutil
print("Running")
def sort_labels(base_path, image_folders, label_folder):
    # Loop through each subfolder in the images directory
    for folder in image_folders:
        image_dir = os.path.join(base_path, 'images', folder)
        label_dir = os.path.join(base_path, 'labels', folder)
        
        # Create corresponding label subdirectories if they don't exist
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        
        # Get list of images in the current image subdirectory
        images = [img for img in os.listdir(image_dir) if img.endswith('.jpg')]
        
        # Move each corresponding .txt file to the appropriate label subdirectory
        for img in images:
            txt_filename = img.replace('.jpg', '.txt')
            src_txt_path = os.path.join(base_path, 'labels', txt_filename)
            dest_txt_path = os.path.join(label_dir, txt_filename)
            
            # Check if the annotation file exists in the main label folder
            if os.path.exists(src_txt_path):
                shutil.move(src_txt_path, dest_txt_path)
            else:
                print(f"Annotation file not found for {src_txt_path}")

# Define your base path where 'images' and 'labels' directories are located
base_path = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\yolov5\\data'
image_folders = ['train', 'val', 'test']  # Include 'test' if you're using it
label_folder = 'labels'

# Call the function
sort_labels(base_path, image_folders, label_folder)
print("Finished")