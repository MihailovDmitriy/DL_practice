
import os
import sys
import scipy.io
import scipy.misc
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
#from net_utils import *
import numpy as np
import tensorflow as tf

%matplotlib inline

content_image = scipy.misc.imread("images/louvre.jpg")
imshow (content_image)