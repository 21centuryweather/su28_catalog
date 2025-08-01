import pathlib
from ecgtools import Builder
from parse_filenames import parse_himawari

cat_builder = Builder(
    # Directory with the output
    paths=['/g/data/su28/himawari-ahi/'],
    # Depth of 1 since we are sending it to the case output directory
    depth=3,
    # Number of jobs to execute - should be equal to # threads you are using
    joblib_parallel_kwargs={'n_jobs': 6},
)
cat_builder = cat_builder.build(parsing_func = parse_himawari)

cat_builder.invalid_assets

cat_builder.save(
    name='himawari_ahi_cloud',
    directory='/g/data/su28/tools/su28_catalog/catalog/himawari_ahi_cloud/',
    # Column name including filepath
    path_column_name='path',
    # Column name including variables
    variable_column_name='variable',
    # Data file format - could be netcdf or zarr (in this case, netcdf)
    data_format="zarr",
    # Which attributes to groupby when reading in variables using intake-esm
    groupby_attrs=["variable"],
    # Aggregations which are fed into xarray when reading in data using intake
    aggregations=[
        {
            "type": "join_existing",
            "attribute_name": "time",
            "options": {"dim": "time", "coords": "minimal", "compat": "override"},
        },
    ],
    description='The cloud type product is derived from Himawari AHI data using NWC SAF algorithms. The CT product contains information on the major cloud classes. INFO: https://21centuryweather.github.io/21st-Century-Weather-Software-Wiki/datasets/himawari-ahi.html',
)