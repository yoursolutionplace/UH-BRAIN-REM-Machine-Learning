# -*- coding: utf-8 -*-
"""
@author: Mikhilesh Seepana
"""

# === USER SETTINGS ===
jpg_image_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_2_crop_cropped_images_for_machine_learning\cropped_volume_1\vol1_096.jpg"
nii_file_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_4_5_load_into_3d_slicer_and_export_segmentation\volume1\volume1.nii.gz"
slice_index = 94  # Example: vol2_088.jpg → 88 - 1 = 87

# === SCRIPT START ===
import os
import numpy as np
import nibabel as nib
from PIL import Image
import matplotlib.pyplot as plt

def check_alignment(jpg_path, nii_path, slice_idx):
    # Load .jpg image
    jpg_image = Image.open(jpg_path).convert('L')
    jpg_array = np.array(jpg_image)

    # Load .nii.gz and get shape
    nii_image = nib.load(nii_path)
    nii_array = nii_image.get_fdata()

    # Decide which axis is the slice axis (Z axis)
    if nii_array.shape[0] == 100:
        nii_slice = nii_array[slice_idx, :, :]
    elif nii_array.shape[2] == 100:
        nii_slice = nii_array[:, :, slice_idx]
    else:
        raise ValueError("Cannot determine slice direction. Check volume shape:", nii_array.shape)

    nii_slice = np.uint8(np.round(nii_slice))  # ensure displayable

    # Plot side-by-side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(jpg_array, cmap='gray')
    axs[0].set_title(os.path.basename(jpg_path))
    axs[0].axis('off')

    axs[1].imshow(nii_slice, cmap='gray')
    axs[1].set_title(f"Slice {slice_idx} from {os.path.basename(nii_path)}")
    axs[1].axis('off')

    plt.tight_layout()
    plt.show()

# === Run Function ===
check_alignment(jpg_image_path, nii_file_path, slice_index)
