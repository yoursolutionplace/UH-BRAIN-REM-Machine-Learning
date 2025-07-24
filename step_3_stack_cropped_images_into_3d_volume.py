# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:22:39 2025

@author: Mikhilesh Seepana
"""

import os
import numpy as np
import nibabel as nib
from PIL import Image

# === SETTINGS ===
input_base_dir = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_2_crop_cropped_images_for_machine_learning"
output_base_dir = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_3_stack_cropped_images_into_3d_volume"
volume_names = ["cropped_volume_1", "cropped_volume_2", "cropped_volume_3", "cropped_volume_4"]

os.makedirs(output_base_dir, exist_ok=True)

for vol_index, volume in enumerate(volume_names, start=1):
    input_folder = os.path.join(input_base_dir, volume)
    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')])

    slices = []
    for file_name in image_files:
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path).convert('L')
        slices.append(np.array(img))

    volume_array = np.stack(slices, axis=0).astype(np.uint8)  # shape: (Z, Y, X)
    nifti_img = nib.Nifti1Image(volume_array, affine=np.eye(4))

    out_path = os.path.join(output_base_dir, f"volume{vol_index}.nii.gz")
    nib.save(nifti_img, out_path)

print("All 4 volumes successfully saved as .nii.gz.")
