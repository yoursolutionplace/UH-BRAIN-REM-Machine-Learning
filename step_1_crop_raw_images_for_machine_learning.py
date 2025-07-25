# -*- coding: utf-8 -*-
"""
@author: Mikhilesh Seepana
"""

from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np

# Function to crop and save in grayscale using matplotlib
def crop_image_gray(image_path, output_path, crop_area):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_area)

    # Convert to grayscale
    grayscale_image = cropped_image.convert('L')

    # Convert to numpy array for applying colormap
    grayscale_array = np.array(grayscale_image)

    # Save the image using matplotlib with cmap='gray'
    plt.imsave(output_path, grayscale_array, cmap='gray', format='png')

# Folder containing the images
input_folder_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Input\2008-rat-somatosensory-nissl"
output_folder_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_1_crop_raw_images_for_machine_learning"

# Create output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Crop area (left, upper, right, lower)
crop_area = (1625, 4870, 2225, 5570)

# Loop through each image in the folder
count = 0
for filename in os.listdir(input_folder_path):
    if filename.lower().endswith(('.jpg', '.png', '.tif')):
        image_path = os.path.join(input_folder_path, filename)
        output_path = os.path.join(output_folder_path, os.path.splitext(filename)[0] + '.png')  # Save all as .png
        crop_image_gray(image_path, output_path, crop_area)
        count += 1

print(f"{count} images cropped and saved to: {output_folder_path}")
