import numpy as np
def test_random():
    mean = 25
    sdev = 3
    sample_size = 4000000

    sample = np.random.normal(mean, sdev, sample_size)
    np.testing.assert_almost_equal(mean, np.mean(sample), decimal=2)
    np.testing.assert_almost_equal(sdev, np.std(sample), decimal=2)