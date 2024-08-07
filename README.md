# EXPERIMENTAL TOOLS

Here you can find a set of experimental tools; this code is provided as-is, with no support or warranty.

&nbsp;

---

<h1 style="color: lightcoral;">DATASET REPORT GENERATOR</h1>

This script generates a comprehensive report for a dataset. It fetches data from the MVI API, processes the images and labels, and creates a detailed report in HTML, PDF, and Excel formats.

### Features

- Filters files based on date range or quantity
- Processes images and labels, creating annotated images
- Generates an Excel report with existing labels data
- Creates pie charts for label distribution
- Generates HTML and PDF reports with detailed information and statistics

### Requirements

Python 3.6 or higher installed; the necessary packages can be installed via pip:

```bash
pip install argparse jinja2 matplotlib opencv-python-headless openpyxl pandas Pillow requests weasyprint
```

### Usage

Run the script with the following command:

```bash
python3 dataset_report_generator.py url api_key dataset_id --files <number_of_files> --start-date "dd-MMM-yyyy" --end-date "dd-MMM-yyyy"
```

(an example of date format dd-MMM-yyyy is: 01-Jan-2000)

#### Parameters

- url: the base URL of the API
- api_key: the API key for authentication
- dataset_id: the ID of the dataset to be processed
- --files: (optional) the number of files to process
- --start-date: (optional) the start date for filtering files (format: dd-MMM-yyyy)
- --end-date: (optional) the end date for filtering files (format: dd-MMM-yyyy)
- **if the optional parameters are not included, a report with the entire contents of the dataset will be generated.**

## Licenses

- **argparse**: Distributed under the [Python Software Foundation License Version 2](https://github.com/python/cpython/blob/main/LICENSE).
- **cv2 (OpenCV)**: Distributed under the [Apache License 2.0](https://github.com/opencv/opencv/blob/master/LICENSE).
- **matplotlib**: Distributed under the [Matplotlib License (BSD-style)](https://matplotlib.org/stable/project/license.html).
- **opencv-python-headless**: Distributed under the [MIT License](https://github.com/opencv/opencv-python/blob/4.x/LICENSE.txt).
master/LICENCE).
mqtt.python/blob/master/LICENSE.txt).
- **pandas**: Distributed under the [BSD 3-Clause License](https://github.com/pandas-dev/pandas/blob/main/LICENSE).
- **requests**: Distributed under the [Apache License 2.0](https://github.com/psf/requests/blob/main/LICENSE).
