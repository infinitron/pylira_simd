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
