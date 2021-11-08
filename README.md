pylira_simd
==============

|      CI              | status |
|----------------------|--------|
| pip builds           | ![example workflow](https://github.com/infinitron/pylira_simd/actions/workflows/pip.yml/badge.svg)

Python bindings for [LIRA](https://github.com/astrostat/pylira/) with SIMD intrinsics.

Installation
------------

```bash
sudo apt install libtbb-dev r-base-dev r-base electric-fence r-mathlib
git clone --recursive https://github.com/infinitron/pylira_simd
pip install ./pylira_simd
```

Usage
------------
```python
from pylira_simd import image_analysis
image_analysis(...)
```
