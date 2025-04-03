import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

# Define paths
data_folder = "IXI-T1.nosync"
slice_index = 135  # Middle slice

k_space_data = []

# Loop through all .nii files in the folder
nii_img = nib.load("IXI-T1.nosync/IXI012-HH-1211-T1.nii")

img_data = nii_img.get_fdata()
print(img_data.shape)

# Extract the middle slice
slice_2D = img_data[:,  slice_index,:]

plt.imshow(slice_2D)
plt.show()

k_space = np.fft.fft2(slice_2D)
k_space = np.fft.fftshift(k_space)

plt.imshow(np.abs(k_space))
plt.show()