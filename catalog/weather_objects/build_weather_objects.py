import pathlib
from ecgtools import Builder
from parse_filenames import parse_weather_objects

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/weatherfeatures.era5/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=4,
    # Exclude the timeseries and restart directories
    exclude_patterns=["*/fronts/*", "*/clim/*", "*/docu/*", "*/run/*", "*/tracks/*", "*/cdf.3dmask/*"],
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': 6},
)

cat_builder = cat_builder.build(parsing_func = parse_weather_objects)

cat_builder.invalid_assets

cat_builder.save(
    name='weather_objects',
    directory='/g/data/su28/tools/su28_catalog/catalog/weather_objects/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='variable',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable", "frequency", "resolution", "year", "month"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='ERA5-based Weather Objects includes anticyclones (maxcl), cyclones (mincl) and warm-conveyor belts (wcb). INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/weather_objects.html',
)