import pathlib
import re
import xarray as xr

def parse_daily_era5 (file):

    """
    Parse filename and metadata for /g/data/su28/ERA5/daily/2t/2t_era5_oper_sfc_merge_1deg_daily_2024.nc like files.
    """

    # Default arguments to open metadata
    _default_kwargs = {'engine': 'netcdf4', 'chunks': {}, 'decode_times': False}
    xarray_open_kwargs = _default_kwargs
    
    file = pathlib.Path(file)
    z  = file.stem.split('_') # Split elements in filename using "_"
    print(file)
    info = {}
    info['variable'] = z[0]
    info['dataset'] = z[1]
    info['level'] = z[3]
    info['resolution'] = z[5]
    info['frequency'] = z[6]
    info['year'] = z[7]

    with xr.open_dataset(file, **xarray_open_kwargs) as ds:
        if info['variable'] in list(ds.data_vars): # check that variable is the file

            info['name_in_file'] = info['variable']
            # Get the long name from dataset
            info['long_name'] = ds[info['variable']].attrs.get('long_name')
            # Grab the units of the variable
            info['units'] = ds[info['variable']].attrs.get('units')

        else: # guess variable

            info['name_in_file'] = list(ds.data_vars)[-1]
            # Get the long name from dataset
            info['long_name'] = ds[list(ds.data_vars)[-1]].attrs.get('long_name')
            # Grab the units of the variable
            info['units'] = ds[list(ds.data_vars)[-1]].attrs.get('units')

    info['path'] = file
    
    return info


def parse_drought_era5 (file):

    """
    Parse filename and metadata for /g/data/su28/drought_era5/SPI/12m/SPI12_gamma_global_era5_moda_ref1991to2020_202403.nc like files.
    """

    # Default arguments to open metadata
    _default_kwargs = {'engine': 'netcdf4', 'chunks': {}, 'decode_times': False}
    xarray_open_kwargs = _default_kwargs
    
    file = pathlib.Path(file)
    z  = file.stem.split('_') # Split elements in filename using "_"
    var_accum = re.findall(r'[A-Za-z]+|\d+', z[0])
    print(file)

    info = {}
    info['variable'] = var_accum[0]
    info['dataset'] = 'drought_era5'
    info['accumulation'] = var_accum[1]
    info['resolution'] = 0.25
    info['frequency'] = 'montly'
    info['year_month'] = z[6]
    info['reference'] = z[5]

    with xr.open_dataset(file, **xarray_open_kwargs) as ds:
        if info['variable'] in list(ds.data_vars): #check that variable is the file

            info['name_in_file'] = info['variable']
            # Get the long name from dataset
            info['long_name'] = ds[info['variable']].attrs.get('long_name')

        else: #guess variable

            info['name_in_file'] = list(ds.data_vars)[-1]
            # Get the long name from dataset
            info['long_name'] = ds[list(ds.data_vars)[-1]].attrs.get('long_name')

    info['path'] = file
    
    return info
