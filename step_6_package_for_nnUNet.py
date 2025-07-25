# -*- coding: utf-8 -*-
"""
Step 6 - Package data for nnUNet (Fixed JSON formatting)
@author: Mikhilesh Seepana
"""

import os
import shutil
import json

# === CONFIG ===
volume_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_4_5_load_into_3d_slicer_and_export_segmentation\cropped_volume.nii.gz"
label_path = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_4_5_load_into_3d_slicer_and_export_segmentation\cropped_volume_seg.nii.gz"
nnunet_base = r"C:\Users\Mikhilesh\Desktop\REM Project\Image Analysis\Output\step_6_package_for_nnUNet\nnunet_data"
dataset_name = "Dataset001_MikhileshCells"

# === STEP 1: Check input files ===
if not os.path.exists(volume_path):
    raise FileNotFoundError(f"Volume file not found: {volume_path}")
if not os.path.exists(label_path):
    raise FileNotFoundError(f"Segmentation file not found: {label_path}")

print("Input files verified.")

# === STEP 2: Create nnUNet folder structure ===
dataset_path = os.path.join(nnunet_base, dataset_name)
imagesTr_path = os.path.join(dataset_path, "imagesTr")
labelsTr_path = os.path.join(dataset_path, "labelsTr")

os.makedirs(imagesTr_path, exist_ok=True)
os.makedirs(labelsTr_path, exist_ok=True)

print(f"Created folders:\n - {imagesTr_path}\n - {labelsTr_path}")

# === STEP 3: Copy files ===
volume_target = os.path.join(imagesTr_path, "case001_0000.nii.gz")  # _0000 = modality 0
label_target = os.path.join(labelsTr_path, "case001.nii.gz")

shutil.copy(volume_path, volume_target)
shutil.copy(label_path, label_target)

print(f"Copied volume to: {volume_target}")
print(f"Copied label to: {label_target}")

# === STEP 4: Create dataset.json (Fully nnUNet v2 compatible) ===
dataset_json = {
    "name": "MikhileshCells",
    "description": "Single 3D volume and segmentation of rat tissue nuclei annotated in 3D Slicer",
    "tensorImageSize": "3D",
    "file_ending": ".nii.gz",
    "channel_names": {
        "0": "channel0"   # Change to "histology" or "fluorescence" if appropriate
    },
    "labels": {
        "0": "background",
        "1": "cell"
    },
    "numTraining": 1,
    "training": [
        {
            "image": "imagesTr/case001_0000.nii.gz",
            "label": "labelsTr/case001.nii.gz"
        }
    ],
    "test": []
}

json_path = os.path.join(dataset_path, "dataset.json")
with open(json_path, "w") as f:
    json.dump(dataset_json, f, indent=4)

print("dataset.json created successfully at:", json_path)
print("nnUNet dataset is ready at:", dataset_path)
