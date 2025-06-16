import pathlib
from ecgtools import Builder
from parse_filenames import parse_MMLEAv2

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/MMLEAv2/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=5,
    # Exclude the timeseries and restart directories
    exclude_patterns=["*.ipynb_checkpoints*", "*/observations/*"],
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': 6},
)

cat_builder = cat_builder.build(parsing_func = parse_MMLEAv2)

cat_builder.invalid_assets

cat_builder.save(
    name='MMLEAv2',
    directory='/g/data/su28/tools/su28_catalog/catalog/MMLEAv2/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='variable',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="netcdf",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable", "frequency", "model", "experiment", "resolution", "time_range"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time_range",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='The Multi-Model Large Ensemble Archive version 2 (MMLEAv2) includes 18 models (12 CMIP6 and 6 CMIP5) and 15 monthly variables. INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/mmleav2.html',
)