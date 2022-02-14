# import basic homogeneous transformations
import p2_sol as p2
# import numpy for matrix multiplication
import numpy as np
import math

def main():

	# update output format
	np.set_printoptions(precision = 2, suppress = True)

	### Transformation 1 (Current Frame)
	# Translation of 2.5 units on x-axis
	H_1 = p2.trans_x(2.5)
	# Translation of 0.5 units on z-axis
	H_1 = np.matmul(H_1, p2.trans_z(0.5))
	# Translation of -1.5 units on y-axis
	H_1 = np.matmul(H_1, p2.trans_y(-1.5))
	
	print("The result of Transformation 1 (transformations in CURRENT FRAME) is:\n", H_1)
	
	### Transformation 2 (Current Frame)
	# Translation of 0.5 units on z-axis
	H_2 = p2.trans_z(0.5)
	# Translation of 2.5 units on x-axis
	H_2 = np.matmul(H_2, p2.trans_x(2.5))
	# Translation of -1.5 units on y-axis
	H_2 = np.matmul(H_2, p2.trans_y(-1.5))

	print("The result of Transformation 2 (transformations in CURRENT FRAME) is:\n", H_2)
	
	### Transformation 3 (Fixed Frame)
	# Translation of 2.5 units on x-axis
	H_3 = p2.trans_x(2.5)
	# Translation of 0.5 units on z-axis
	H_3 = np.matmul(p2.trans_z(0.5), H_3)
	# Translation of -1.5 units on y-axis
	H_3 = np.matmul(p2.trans_y(-1.5), H_3)
	
	print("The result of Transformation 3 (transformations in FIXED FRAME) is:\n", H_3)
	
	### Transformation 4 (Fixed Frame)
	# Translation of 0.5 units on z-axis
	H_4 = p2.trans_z(0.5)
	# Translation of 2.5 units on x-axis
	H_4 = np.matmul(p2.trans_x(2.5), H_4)
	# Translation of -1.5 units on y-axis
	H_4 = np.matmul(p2.trans_y(-1.5), H_4)
	
	print("The result of Transformation 4 (transformations in FIXED FRAME) is:\n", H_4)
	
	### Transformation 5 (Current Frame)
	# Rotation of angle pi/2 about x-axis
	H_5 = p2.rot_x(math.pi/2)
	# Translation of 3 units on x-axis
	H_5 = np.matmul(H_5, p2.trans_x(3))
	# Translation of -3 units on z-axis
	H_5 = np.matmul(H_5, p2.trans_z(-3))
	# Rotation of angle pi/2 about z-axis
	H_5 = np.matmul(H_5, p2.rot_z(math.pi/2))
	
	print("The result of Transformation 5 (transformations in CURRENT FRAME) is:\n", H_5)
	
	
	
	print("\n\nThis isnt apart of the assignment, I just wanted to see the result of Transformation 5 in a fixed frame")
	### Transformation 6 (Fixed Frame)
	# Rotation of angle pi/2 about x-axis
	H_6 = p2.rot_x(math.pi/2)
	# Translation of 3 units on x-axis
	H_6 = np.matmul(p2.trans_x(3), H_6)
	# Translation of -3 units on z-axis
	H_6 = np.matmul(p2.trans_z(-3), H_6)
	# Rotation of angle pi/2 about z-axis
	H_6 = np.matmul(p2.rot_z(math.pi/2), H_6)
	
	print("The result of Transformation 6 (transformations in FIXED FRAME) is:\n", H_6)

if __name__ == '__main__':
	main()
