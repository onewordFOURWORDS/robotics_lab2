# import required modules
import numpy as np
import rbm
import math

def main():
	# define rotation values
	psi = math.pi/2
	theta = math.pi/2 
	phi = math.pi/2 
	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	
	# Calculate rotations using values defined in the lab
	# roll rotation about x0
	Rx = rbm.rot_x(psi)
	# pitch rotation about y0
	Ry = rbm.rot_y(theta)
	# pitch rotation about z0
	Rz = rbm.rot_z(phi)
	
	# calculate a total rotation via FIXED FRAME
	R = np.matmul(Rz, Ry, Rx)
	print('The results of the Roll-Pitch-Yaw rotation is:\n',R)
	
if __name__ == '__main__':
	main()
