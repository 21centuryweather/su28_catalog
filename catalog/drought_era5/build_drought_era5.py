import pathlib
from ecgtools import Builder
from parse_filenames import parse_drought_era5

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/drought_era5/SPI/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=2,
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': -1},
)

cat_builder = cat_builder.build(parsing_func = parse_drought_era5)

cat_builder.invalid_assets

cat_builder.save(
    name='drought_era5',
    directory='/g/data/su28/tools/su28_catalog/catalog/drought_era5/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='name_in_file',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable", "accumulation", "reference", "year_month"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time_range",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='Monthly drought indices from 1940 to present derived from ERA5 reanalysis is a global reconstruction of drought indices from 1940 to present. INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/drought-era5.html',
)