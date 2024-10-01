import numpy as np
import math
from scipy import signal
from PIL import Image

def normxcorr2D(image, template):
    t = np.asarray(template, dtype=np.float64)
    t = t - np.mean(t)
    norm = math.sqrt(np.sum(np.square(t)))
    if norm != 0:
        t = t / norm

    sum_filter = np.ones(np.shape(t))

    a = np.asarray(image, dtype=np.float64)
    aa = np.square(a)

    a_sum = signal.correlate(a, sum_filter, 'same')
    aa_sum = signal.correlate(aa, sum_filter, 'same')

    numer = signal.correlate(a, t, 'same')
    denom = np.sqrt(aa_sum - np.square(a_sum)/np.size(t))

    tol = np.sqrt(np.finfo(denom.dtype).eps)
    nxcorr = np.where(denom < tol, 0, numer/denom)
    nxcorr = np.where(np.abs(nxcorr-1.) > np.sqrt(np.finfo(nxcorr.dtype).eps), nxcorr, 0)

    return np.mean(nxcorr)

def test_ncorr():
    image = Image.open('../Input.png')
    contrast_image = Image.open('../Output.png')
    print(f"Mean NCORR value is {normxcorr2D(image, contrast_image)}")

if __name__ == '__main__':
    test_ncorr()

