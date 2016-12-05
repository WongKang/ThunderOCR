import numpy as np

# ************************************************
# Function : Generate random color in range of [0,255]
def generate_random_color():
	return (np.random.rand(1,3)[0]*255).astype(np.int32).tolist()

