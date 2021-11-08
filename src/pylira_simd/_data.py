import importlib.resources as importlib_resources
from astropy.io import fits
import numpy as np


def _read_sample_fits(file_name):
    pkg = importlib_resources.files("pylira_simd")
    with importlib_resources.as_file(pkg / "sample_data" / "img_64x64.fits") as img_path:
        with fits.open(img_path) as hdul:
            return hdul[0].data

class _dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def get_sample_images():
    _img_64x64_dat = _read_sample_fits("img_64x64.fits")
    _psf_33x33 = _read_sample_fits("psf_33x33.fits")
    _baseline_64x64 = _read_sample_fits("null_q1_c1.fits")
    _expmap_64x64 = np.ones((64, 64))
    _start_64x64 = np.ones((64, 64))

    return _dotdict(dict(img_64x64=_img_64x64_dat, psf_33x33=_psf_33x33, baseline_64x64=_baseline_64x64, expmap_64x64=_expmap_64x64, start_64x64=_start_64x64))

