#first file in repo
#open .nc file 
import netCDF4 as nc
fn = '/Users/ryanfriess/Desktop/solarcar/cloud-cover/nc-files/file1.nc'
ds = nc.Dataset(fn)

def process_array(mask_array):
    new_array = [[0 for _ in range(len(mask_array[0]))] for _ in range(len(mask_array))]
    for r in range(len(mask_array)):
        for c in range(len(mask_array[0])):
            new_array[r][c] = mask_array[r][c]

    return new_array

def write_to_file(fn, img):
    height, width = str(len(img)), str(len(img[0]))
    fwith open("/output-files/"+fn, 'w') as f:
        f.write("P3\n")
        f.write(width + " " + height +"\n")
        f.write("255\n")  # Maximum color value

        # Write pixel data
        for r in range(len(img)):x
            f.write(f"{r} {g} {b} ")
        f.write("\n")

# Access the Cloud_Mask variable
cloud_mask = ds.groups['geophysical_data'].variables['Cloud_Mask'][:]

# Print out the cloud mask data
print("Number of images (first dimension of cloud_mask):" , len(cloud_mask))
for i in range(len(cloud_mask)):
    print("Dimension of image " + str(i) + ":", len(cloud_mask[i]), len(cloud_mask[i][i]))
    mask_array = cloud_mask[i]
    # print(mask_array[0][0])
    processed = process_array(mask_array)






'''
# List the groups
print(ds.groups)

# Check variables inside 'geolocation_data' group
geolocation_group = ds.groups['geolocation_data']
print(geolocation_group.variables)

# Check variables inside 'geophysical_data' group
geophysical_group = ds.groups['geophysical_data']
print(geophysical_group.variables)

'''