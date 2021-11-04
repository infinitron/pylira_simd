#include "lira.cpp"

#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;
using namespace pybind11::literals;

namespace hwy {
namespace lira {

using np_arr_d = py::array_t<double>;
using d_ptr = double*;

np_arr_d
image_analysis(
  np_arr_d t_obs,
  np_arr_d t_start,
  np_arr_d t_psf,
  np_arr_d t_expmap,
  np_arr_d t_baseline,
  std::string t_out_file,
  std::string t_param_file,
  np_arr_d t_alpha_init,
  int t_max_iter,
  int t_burn_in,
  int t_save_thin,
  bool t_fit_bkgscl,
  double t_ms_ttlcnt_pr,
  double t_ms_ttlcnt_exp,
  double t_ms_al_kap1,
  double t_ms_al_kap2,
  double t_ms_al_kap3,
  int t_use_float,
  int is_psf_prag_bayesian)
{
    auto obs_buf = t_obs.request();
    auto start_buf = t_start.request();
    auto psf_buf = t_start.request();
    auto baseline_buf = t_baseline.request();
    auto expmap_buf = t_expmap.request();
    auto alpha_buf = t_alpha_init.request();

    char* out_file_name = const_cast<char*>(t_out_file.c_str());
    char* param_file_name = const_cast<char*>(t_param_file.c_str());

    int nrows_obs = obs_buf.shape[0];
    int ncols_obs = obs_buf.shape[1];
    int nrows_psf = psf_buf.shape[0];
    int ncols_psf = psf_buf.shape[1];
    int nvals_alpha = psf_buf.shape[0];

    //allocate the post_mean memory
    auto post_mean = np_arr_d(obs_buf.size);
    auto post_mean_buf = post_mean.request();

    d_ptr obs_arr = static_cast<d_ptr>(obs_buf.ptr);
    d_ptr start_arr = static_cast<d_ptr>(start_buf.ptr);
    d_ptr psf_arr = static_cast<d_ptr>(psf_buf.ptr);
    d_ptr expmap_arr = static_cast<d_ptr>(expmap_buf.ptr);
    d_ptr alpha_int_arr = static_cast<d_ptr>(alpha_buf.ptr);
    d_ptr post_mean_arr = static_cast<d_ptr>(post_mean_buf.ptr);
    d_ptr baseline_arr = static_cast<d_ptr>(baseline_buf.ptr);

    //dummy values for unused params in the C code
    //TODO: remove these arguments from the image_analysis_R function
    d_ptr dummy;
    int true_int = 1;

    image_analysis_lira(dummy, post_mean_arr, obs_arr, start_arr, psf_arr, expmap_arr, baseline_arr, &out_file_name, &param_file_name, &t_max_iter, &t_burn_in, &true_int, &true_int, &nrows_obs, &ncols_obs, &nrows_psf, &ncols_psf, &true_int, &true_int, alpha_int_arr, &nvals_alpha, &t_ms_ttlcnt_pr, &t_ms_ttlcnt_exp, &t_ms_al_kap2, &t_ms_al_kap1, &t_ms_al_kap3, &t_use_float, &is_psf_prag_bayesian);

    post_mean.resize({ nrows_obs, ncols_obs });

    return post_mean;
}

}
}