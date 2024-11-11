import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


fn = '/Users/samba/Documents/WeatherData/file1.nc'
ds = nc.Dataset(fn)

cloud_mask = ds.groups['geophysical_data'].variables['Cloud_Mask'][:]
print(f"Cloud Mask Shape: {cloud_mask.shape}")

# Loop through each layer of the cloud mask data
for i in range(cloud_mask.shape[0]):
   plt.figure(figsize=(10, 8)) 
   plt.imshow(cloud_mask[i], cmap='gray', interpolation='nearest')  
   plt.colorbar(label='Cloud Mask Value')  
   plt.title(f'Cloud Mask Visualization - Layer {i + 1}')  
   plt.axis('off')  
   plt.show()  


ds.close()
