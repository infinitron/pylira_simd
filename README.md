pylira_simd
==============

|      CI              | status |
|----------------------|--------|
| pip builds           | [![Pip Actions Status][actions-pip-badge]][actions-pip-link] |

Python bindings for [LIRA](https://github.com/astrostat/pylira/) with SIMD intrinsics.

Installation
------------

- `sudo apt install libtbb-dev r-base-dev r-base electric-fence r-mathlib`
- `git clone --recursive https://github.com/infinitron/pylira_simd`
- `pip install ./pylira_simd`

Usage
------------
```python
from pylira_simd import image_analysis
image_analysis(...)
```
