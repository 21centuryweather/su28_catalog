# `su28` intake data catalog

An intake data catalog is a easy way to access a dataset (usually composed of many files). It is also useful to discover new datasets available and list variables, date ranges and other attributes. The catalog will also alow you to load the data to start working.

(almost) all datasets hosted on su28 and documented in this wiki are listed in the su28 catalog. The catalog can be access through the url or from Gadi:

```python
catalog_url = intake.open_catalog("https://raw.githubusercontent.com/21centuryweather/su28_catalog/refs/heads/main/catalog/su28_catalog.yaml")
catalog_path = intake.open_catalog("/g/data/su28/tools/su28_catalog/catalog/su28_catalog.yaml")
```

An example on how to use this catalog can be found [here](https://github.com/21centuryweather/su28_catalog/blob/main/docs/how_to_catalog.ipynb).

---

This repository includes the necesary code to build the `su28` catalog. If you want to add a new dataset, plase open an issue. 
