import pylira_simd as m


def test_version():
    assert m.__version__ == "0.1.0"


def test_add():
    assert m.add(1, 2) == 3


def test_sub():
    assert m.subtract(1, 2) == -1


def test_exports_image_analysis():
    assert m.image_analysis is not None


def test_exports_data():
    assert m.get_sample_images() is not None

def test_test_payload():
    test_payload = m.get_test_payload()
    sample_images = m.get_sample_images()
    assert (test_payload.observation==sample_images.img_64x64).all()
    assert (test_payload.psf==sample_images.psf_33x33).all()
    assert (test_payload.baseline==sample_images.baseline_64x64).all()
    assert (test_payload.exp_map==sample_images.expmap_64x64).all()
    assert (test_payload.start_map==sample_images.start_64x64).all()

def test_run_lira():
    test_payload = m.get_test_payload()
    test_payload.max_iter=5
    test_payload.burn_in=1
    test_payload.thin=1
    test_payload.out_param_file="out.param"
    test_payload.out_img_file="img.out"
    #check if it runs without exceptions
    assert test_payload.run_image_analysis() is not None
