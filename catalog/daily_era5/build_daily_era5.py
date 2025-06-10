import pathlib
#import intake
from ecgtools import Builder
#import xarray as xr
from parse_filenames import parse_daily_era5

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/ERA5/daily'],
    # Depth of 1 since we are sending it to the case output directory
    depth=2,
    # Exclude landmask 
    exclude_patterns=["*/ldmk/*"],
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': -1},
)

cat_builder = cat_builder.build(parsing_func = parse_daily_era5)

cat_builder.invalid_assets

cat_builder.save(
    name='daily_era5',
    directory='/g/data/su28/tools/su28_catalog/catalog/daily_era5/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='name_in_file',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {'type': 'union', 'attribute_name': 'variable'},
        {
            "type": "join_existing",
            "attribute_name": "time_range",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='ERA5 is a climate reanalysis dataset, covering the period 1950 to present. This dataset includes 2d and 3d common variables in daily frequency. The data was also remaped from 0.25 degree to 1 degree. INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/daily-era5.html',
)