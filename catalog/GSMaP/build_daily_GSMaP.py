import pathlib
from ecgtools import Builder
from parse_filenames import parse_GSMaP

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/GSMaP/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=5,
    # Exclude the timeseries and restart directories
    exclude_patterns=["*/docs/*", "*/raw/*", "*pdf", "*txt"],
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': 6},
)

cat_builder = cat_builder.build(parsing_func = parse_GSMaP)

cat_builder.invalid_assets

cat_builder.save(
    name='GSMaP',
    directory='/g/data/su28/tools/su28_catalog/catalog/GSMaP/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='variable',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable", "frequency", "version", "resolution", "year_month"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='Global Satellite Mapping of Precipitation (GSMaP) includes daily precipitation in 0.1 degree resolution. INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/gsmap.html',
)