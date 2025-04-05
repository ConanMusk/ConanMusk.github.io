#%%
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
input_path = '/home/cyh/Code/2025/ConanMusk.github.io/images/DeRain-VSBL.jpg'
img = (Image.open(input_path)).convert("RGB")
img = np.array(img)
# %%
plt.imshow(img)
plt.show()
