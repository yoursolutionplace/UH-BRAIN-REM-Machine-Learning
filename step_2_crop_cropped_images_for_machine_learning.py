# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 07:38:03 2025

@author: Mikhilesh Seepana
"""

import os
from PIL import Image

input_base_dir = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_2_crop_cropped_images_for_machine_learning"
output_base_dir = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_2_crop_cropped_images_for_machine_learning"
volume_names = ["cropped_volume_src_1", "cropped_volume_src_2", "cropped_volume_src_3", "cropped_volume_src_4"]
center_crop_size = 100

def center_crop(img, crop_size):
    width, height = img.size
    left = (width - crop_size) // 2
    upper = (height - crop_size) // 2
    right = left + crop_size
    lower = upper + crop_size
    return img.crop((left, upper, right, lower))

for vol_index, volume in enumerate(volume_names, start=1):
    input_folder = os.path.join(input_base_dir, volume)
    output_folder = os.path.join(output_base_dir, f"cropped_volume_{vol_index}")
    os.makedirs(output_folder, exist_ok=True)

    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    for i, file_name in enumerate(image_files):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path).convert('L')
        cropped_img = center_crop(img, center_crop_size)

        out_name = f"vol{vol_index}_{i+1:03d}.jpg"
        out_path = os.path.join(output_folder, out_name)
        cropped_img.save(out_path)

print("Done! Center-cropped 100x100 images saved in 'step_1b_crop_cropped_images_for_machine_learning'.")
