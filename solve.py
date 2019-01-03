#!/usr/bin/env python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
pieces = cv2.imread('./pieces.jpeg')
pieces_bw = cv2.cvtColor(pieces, cv2.COLOR_BGR2GRAY)



# Show image
fig, axs = plt.subplots(1, 1)
pieces_ax = axs[0]
pieces_ax.imshow(pieces_bw, 'gray')

plt.show()
