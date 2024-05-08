import os
import shutil
from sklearn.model_selection import train_test_split

# Define the path to your dataset where the resized images are stored
data_path = 'C:\\Users\\rgsmi\\OneDrive\\CityU\\fgvc-aircraft-2013b\\data\\resized_images'
files = [f for f in os.listdir(data_path) if f.endswith('.jpg')]

# Print out the number of files found to ensure there are images to split
print(f"Total images found: {len(files)}")

# Split data into training and temp (validation + test) with shuffling
train_files, temp_files = train_test_split(files, test_size=0.2, random_state=42)

# Split temp into validation and test
val_files, test_files = train_test_split(temp_files, test_size=0.5, random_state=42)

# Function to move files to their respective directories
def move_files(file_list, src_dir, dest_dir):
    for file in file_list:
        src_file_path = os.path.join(src_dir, file)
        dest_file_path = os.path.join(dest_dir, file)
        shutil.move(src_file_path, dest_file_path)

# Create directories if they don't exist and move files
for folder, file_list in zip(['train', 'val', 'test'], [train_files, val_files, test_files]):
    folder_path = os.path.join(data_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    move_files(file_list, data_path, folder_path)

print("Files distributed: Train {}, Val {}, Test {}".format(len(train_files), len(val_files), len(test_files)))
