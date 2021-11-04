#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

#include "lira_pyb/lira_simd_pyb.cpp"

int add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(_pylira_simd, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: scikit_build_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers

        Some other explanation about the subtract function.
    )pbdoc");

    m.def("image_analysis", &hwy::lira::image_analysis, "observed_im"_a, "start_im"_a, "psf_im"_a, "expmap_im"_a, "baseline_im"_a, "out_img_file"_a, "out_param_file"_a, "alpha_init"_a, "max_iter"_a = 3000, "burn_in"_a = 1000, "save_thin"_a = true, "fit_bkgscl"_a = true, "ms_ttlcnt_pr"_a = 1, "ms_ttlcnt_exp"_a = 0.05, "ms_al_kap1"_a = 0.0, "ms_al_kap2"_a = 1000.0, "ms_al_kap3"_a = 3,"use_float"_a=true,"use_prag_bayesian"_a=true,R"liradoc(
        Uses LIRA to generate images of the added component by comparing the observed image against the baseline.

        Parameters
        ----------
        

    )liradoc");

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
