pylira_simd
==============

|      CI              | status |
|----------------------|--------|
| pip builds           | ![example workflow](https://github.com/infinitron/pylira_simd/actions/workflows/pip.yml/badge.svg)

Python bindings for [LIRA](https://github.com/astrostat/pylira/) with SIMD intrinsics.

Installation
------------

## Linux
```bash
sudo apt install libtbb-dev r-base-dev r-base r-mathlib
git clone --recursive https://github.com/infinitron/pylira_simd
pip install ./pylira_simd
```

## Mac OS
--TBU--

Usage
------------
```python
from pylira_simd import image_analysis, LiraPayload, get_test_payload


# usage 1 (recommended)
# Create a LiraPayload object by supplying at least an input image,
# a baseline image, a psf, and output file names. The images
# can be either fits file names or numpy arrays
...
payload = LiraPayload(inp_image,baseline_image,psf_image,\ 
    out_im_file,out_param)

# Displays input images and prints a table with input params
payload.describe_payload()

payload.launch_image_analysis()

# usage 2
# image_analysis is the low level function used by LiraPayload 
# to run LIRA on the inputs. 
...
...
image_analysis(...)


# Test the program with sample data
payload = get_test_payload()
payload.launch_image_analysis()
```
