import h5py

# 
file_path = '/Users/samba/Documents/WeatherData/T1.hdf'
with h5py.File(file_path, 'r') as file:
    print(file.keys())  # Lists the top-level groups in the file
