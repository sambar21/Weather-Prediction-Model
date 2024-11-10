#first file in repo
#open .nc file 
import netCDF4 as nc
fn = '/Users/samba/Documents/WeatherData/file1.nc'
ds = nc.Dataset(fn)



# Access the Cloud_Mask variable
cloud_mask = ds.groups['geophysical_data'].variables['Cloud_Mask'][:]

# Print out the cloud mask data
print(cloud_mask[0])


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