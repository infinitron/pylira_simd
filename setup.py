import sys
from setuptools import find_packages


try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise


setup(
    name="pylira_simd",
    version="0.1.0",
    description="Python bindings for LIRA with SIMD intrinsics.",
    author="Karthik Reddy",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"pylira_simd": ["sample_data/*.fits"]},
    include_package_data=True,
    cmake_install_dir="src/pylira_simd",
    extras_require={"test": ["pytest","astropy","numpy","tabulate"]},
    python_requires=">=3.9",
)
