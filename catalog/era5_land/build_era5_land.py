import pathlib
from ecgtools import Builder
from parse_filenames import parse_era5_land

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/zz93/era5-land/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=4,
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': 6},
)

cat_builder = cat_builder.build(parsing_func = parse_era5_land)

cat_builder.invalid_assets

cat_builder.save(
    name='era5_land',
    directory='/g/data/su28/tools/su28_catalog/catalog/era5_land/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='name_in_file',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable", "dataset", "level", "resolution", "frequency"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time_range",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='ERA5 land is a land surface dataset forced by ERA5 atmospheric parameters but with no additional data assimilation, covering the period 1950 to present. The collection consists of monthly and sub-daily products from 1950 to the present time.',
)