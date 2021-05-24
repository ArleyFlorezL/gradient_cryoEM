import numpy as np

'''
This .py is used to create the parameters used, which will be in the parameters.txt file and
in the quaternions.txt file.

Here you can create the files with the parameters you'd like.
'''


#Create the parameters file
'''
Explanation of the parameters

Grid Parameters
* NUMBER_PIXELS: quantity of pixels for the grid were the system will be projected
* PIXEL_SIZE: relation between pixels and distance units, e.g: a pixel is equivalent to 1.77 nm

CTF parameters
* CTF_ENV: b parameter for the envelope function defined as env(s) = exp(- b * s^2 / 2)
* CTF_DEFOCUS: defocus used when taking the experimental images
* CTF_AMPLITUDE: 

Modeling with gaussians parameters
* SIGMA: standard deviation for the gaussians with which we model the atoms
* SIGMA_REACH: cut-off for neighbors, only atoms within a n*sigma are considered neighbors

'''

### Change this parameters as you see fit

number_pixels = 124
pixel_size = 1.77

ctf_env = 1.0
ctf_defocus = 1.0
ctf_amplitude = 0.1

sigma = 1
sigma_reach = 3


#LOAD PARAMETERS INTO FILE
params_file = open("data/input/parameters.txt","w")
params_file.write(f"""NUMBER_PIXELS {number_pixels}
PIXEL_SIZE {pixel_size}

CTF_ENV {ctf_env}
CTF_DEFOCUS {ctf_defocus}
CTF_AMPLITUDE {ctf_amplitude}

SIGMA {sigma}
SIGMA_REACH {sigma_reach}
""")
params_file.close()

#Create quaternions file

'''
A quaternion vector is defined as:

q = w + xi + yj + zk

However, when we create a quaternion rotation matrix we read the scalar value last!
'''

w = 0
x = 0
y = 1/np.sqrt(2)
z = 1/np.sqrt(2)

quat_file = open("data/input/quaternions.txt", "w")
quat_file.write(f"{x} {y} {z} {w}")
quat_file.close()