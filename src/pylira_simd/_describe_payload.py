import warnings
from importlib import import_module
from tabulate import tabulate

def _describe_payload(self):
    """
    Displays input images and prints the inputs that will be provided to LIRA
    """
    try:
        plt = import_module("pyplot", package="matplotlib")
    except ImportError:
        warnings.warn(
            "Warning: No matplotlib module found. Input images will not be shown")
    else:
        fig, ax = plt.subplots(2, 3)
        ax[0, 0].imshow(self.observation)
        ax[0, 0].set_title('Input observation', origin='lower')

        ax[0, 1].imshow(self.baseline, origin='lower')
        ax[0, 1].set_title('Baseline model')

        ax[0, 2].imshow(self.psf, origin='lower')
        ax[0, 2].set_title('PSF')

        ax[1, 0].imshow(self.exp_map, origin='lower')
        ax[1, 0].set_title('Exposure map')

        ax[1, 2].imshow(self.start_map, origin='lower')
        ax[1, 2].set_title('Start image')

    print(tabulate(
        [
            ["Input image shape",
                f"{self.observation.shape[0]}x{self.observation.shape[1]}"
             ],
            ["Baseline image shape",
             f"{self.baseline.shape[0]}x{self.baseline.shape[1]}"
             ],
            [
                "PSF shape",
                f"{self.psf.shape[0]}x{self.psf.shape[1]}"
            ],
            [
                "Exposure map shape",
                f"{self.exp_map.shape[0]}x{self.exp_map.shape[1]}"
            ],
            [
                "Start map shape",
                f"{self.start_map.shape[0]}x{self.start_map.shape[1]}"
            ],
            [
                "Initial smoothing params",
                self.alpha_init
            ],
            [
                "Max iterations",
                self.max_iter
            ],
            [
                "Output every",
                f"{self.thin} iterations"
            ],
            [
                "Burn in iterations",
                self.burn_in
            ],
            [
                "Output images path",
                self.out_img_file
            ],
            [
                "Output param file path",
                self.out_param_file
            ],
            [
                "Fit background scale",
                self.fit_bkgscl
            ],
            [
                "Prior on the total count in exposure",
                self.ms_ttlcnt_pr
            ],
            [
                "Prior exposure in units of the actual exposure",
                self.ms_ttlcnt_exp
            ],
            [
                r'\kappa_1',
                self.ms_al_kap1
            ],
            [
                r'\kappa_2',
                self.ms_al_kap2
            ],
            [
                r'\kappa_3',
                self.ms_al_kap3
            ],
            [
                "Working precision",
                "float" if self.use_float else "double"
            ],
            [
                "Use new PSF every 10 iterations",
                self.use_prag_bayesian_psf
            ]

        ]
    ))

    # Use latex to render the prior, if possible
    try:
        _display = import_module("display", "IPython.display")
        _math = import_module("Math", "IPython.display")
        _latex = import_module("Latex", "IPython.display")

        _display(_math(
            fr'\text{{The prior is given by }}(\delta\alpha)^{self.ms_al_kap1} \times \exp({{-{self.ms_al_kap2}\alpha^{self.ms_al_kap3}}})'))
    except ImportError:
        print(
            f'The prior is given by (delta * alpha)^{self.ms_al_kap1} * exp(-{self.ms_al_kap2} * alpha^{self.ms_al_kap3})')
