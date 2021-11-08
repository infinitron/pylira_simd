from ._pylira_simd import image_analysis
from typing import Any
from ._data import get_sample_images
from functools import cached_property
import numpy as np
import numpy.typing as npt
from astropy.io import fits
from typing import Any, Union
from ._describe_payload import _describe_payload


class LiraPayload:
    """
    Provides an interface to set inputs and run LIRA on them.
    """
    _observation = None
    _baseline = None
    _psf = None
    _exp_map = None
    _start_map = None
    _alpha_init = None
    out_img_file = None
    out_param_file = None
    max_iter = None
    _thin = None
    _burn_in = None
    fit_bkgscl = None
    ms_ttlcnt_pr = None
    ms_ttlcnt_exp = None
    ms_al_kap1 = None
    ms_al_kap2 = None
    ms_al_kap3 = None
    use_float = None
    use_prag_bayesian_psf = None

    def __init__(self, observation: Union[str, npt.NDArray[np.number]], baseline: Union[str, npt.NDArray[np.number]],
                 psf: Union[str, npt.NDArray[np.number]], out_img_file: str, out_param_file: str, alpha_init: npt.NDArray[np.number] = None, max_iter: int = 3000, thin: int = 1, burn_in: int = 1000, exp_map: Union[str, npt.NDArray[np.number]] = None, start_map: Union[str, npt.NDArray[np.number]] = None, fit_bkgscl: bool = True, ms_ttlcnt_pr: float = 1, ms_ttlcnt_exp: float = 0.05, ms_al_kap1: float = 0, ms_al_kap2: float = 1000, ms_al_kap3: float = 3, use_float: bool = True, use_prag_bayesian_psf: bool = False) -> None:

        self.observation = observation
        self.baseline = self._get_image_data(baseline)
        self.psf = self._get_image_data(psf)
        self.exp_map = exp_map
        self.start_map = start_map
        self.alpha_init = alpha_init
        self.max_iter = max_iter
        self.thin = thin
        self.burn_in = burn_in
        self.out_img_file = out_img_file
        self.out_param_file = out_param_file
        self.fit_bkgscl = bool(fit_bkgscl)
        self.ms_ttlcnt_pr = ms_ttlcnt_pr
        self.ms_ttlcnt_exp = ms_ttlcnt_exp
        self.ms_al_kap1 = ms_al_kap1
        self.ms_al_kap2 = ms_al_kap2
        self.ms_al_kap3 = ms_al_kap3
        self.use_float = bool(use_float)
        self.use_prag_bayesian_psf = bool(use_prag_bayesian_psf)

    def run_image_analysis(self):
        return image_analysis(self.observation, self.start_map, self.psf, self.exp_map, self.baseline, self.out_img_file, self.out_param_file, self.alpha_init, self.max_iter, self.burn_in,
                              self.thin, self.fit_bkgscl, self.ms_ttlcnt_pr, self.ms_ttlcnt_exp, self.ms_al_kap1, self.ms_al_kap2, self.ms_al_kap3, self.use_float, self.use_prag_bayesian_psf)

    def _get_image_data(self, image: Union(str, npt.NDArray[np.number])):
        if isinstance(image, np.ndarray):
            return image
        elif type(image) is str:
            with fits.open(image) as hdul:
                return hdul[0].data
        else:
            raise ValueError(
                "Input image must be either a file name or a numpy array")

    def describe_payload(self):
        _describe_payload(self)

    @property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, image):
        self._observation = self._get_image_data(image)

    @property
    def baseline(self):
        return self._baseline

    @baseline.setter
    def baseline(self, image):
        self._baseline = self._get_image_data(image)

    @property
    def psf(self):
        return self._psf

    @psf.setter
    def psf(self, image):
        self._psf = self._get_image_data(image)

    @property
    def exp_map(self):
        return self._exp_map

    @exp_map.setter
    def exp_map(self, image):
        if image is None:
            if self._observation is None:
                raise Exception(
                    "exp_map cannot be empty if an input observation is not provided")
            self._exp_map = np.ones(self._observation.shape)
        else:
            self._exp_map = self._get_image_data(image)

    @property
    def start_map(self):
        return self._start_map

    @start_map.setter
    def start_map(self, image):
        if image is None:
            if self._observation is None:
                raise Exception(
                    "start_map cannot be empty if an input observation is not provided")
            self._start_map = np.ones(self._observation.shape)
        else:
            self._start_map = self._get_image_data(image)

    @property
    def alpha_init(self):
        return self._alpha_init

    @alpha_init.setter
    def alpha_init(self, alpha_init_val):
        if self._observation is None:
            raise Exception(
                "alpha_init cannot be set with an empty observation")
        img_dim = self._observation.shape[0]
        if(((img_dim-1) & img_dim) != 0):
            raise Exception(
                "The input image dimensions must be a power of 2")
        im_dim_power2 = np.log2(img_dim)

        if(alpha_init_val is None):
            self._alpha_init = np.asarray(
                [0.3+i*0.1 for i in range(np.log2(img_dim))])
        else:
            if alpha_init_val.shape[0] == im_dim_power2:
                self._alpha_init = alpha_init_val

    @property
    def thin(self):
        return self._thin

    @thin.setter
    def thin(self, thin_val):
        if(thin_val > self.max_iter):
            raise Exception(
                f"thin cannot be greater than max_iter (={self.max_iter})")
        self._burn_in = thin_val

    @property
    def burn_in(self):
        return self._burn_in

    @burn_in.setter
    def burn_in(self, burn_in_val):
        if(burn_in_val > self.max_iter):
            raise Exception(
                f"thin cannot be greater than max_iter (={self.max_iter})")


def get_test_payload():
    """
    Returns a LiraPayload object populated with the sample data.
    The outputs will be stored in the folder LIRA_outputs.
    """
    test_data = get_sample_images()
    return LiraPayload(observation=test_data.img_64x64, baseline=test_data.baseline_64x64, psf=test_data.psf_33x33, out_img_file="LIRA_outputs/img_64x64.out", out_param_file="LIRA_outputs/img_64x64.param")
