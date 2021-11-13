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
import numpy as np

##############################################################
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

###############################################################
# For PSF needing to to be updated dynamically
payload = LiraPayload(inp_image,baseline_image,None,\ 
out_im_file,out_param)
payload.use_prag_bayesian_psf = True

# define a function that returns a new PSF every 10 iterations
def prg_bayes_psf(i):
    if i%10 == 0: #i=0 must always return a non-empty PSF
        return psf #can be from an array, external variable or function
    else:
        return np.ndarray((0,0))

payload.prag_bayes_psf_func = prg_bayes_psf
payload.launch_image_analysis()

###############################################################
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
