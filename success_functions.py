import cv2
from google.colab.patches import cv2_imshow
import numpy as np

def show_merge(img0,img1,img2=None):
  try:
    combined = np.dstack((img0,img1,img2))
  except:
    combined = np.dstack((img0,img1,img0))
  cv2_imshow(combined)


def similarity (img0, img1):
  # Computes Jaccard similarity between the two images (i think the order doesn't really matter)
  return np.logical_and(img0, img1).sum()/np.logical_or(img0, img1).sum()