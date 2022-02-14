# import required modules
import numpy as np
import math

### TRANSLATION MOVEMENTS ###
# basic transformation for translation on x axis
def trans_x(a):
	Tx = np.array([
	[1.0 , 0.0 , 0.0 , a],
	[0.0 , 1.0 , 0.0 , 0.0],
	[0.0 , 0.0 , 1.0 , 0.0],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		  
	return Tx
		
# basic transformation for translation on y axis			
def trans_y(b):
	Ty = np.array([
	[1.0 , 0.0 , 0.0 , 0.0],
	[0.0 , 1.0 , 0.0 , b],
	[0.0 , 0.0 , 1.0 , 0.0],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		  
	return Ty
	
# basic transformation for translation on z axis		
def trans_z(c):
	Tz = np.array([
	[1.0 , 0.0 , 0.0 , 0.0],
	[0.0 , 1.0 , 0.0 , 0.0],
	[0.0 , 0.0 , 1.0 , c],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		
	return Tz
	
### ROTATIONAL MOVEMENTS ###
# basic transformation for rotation about x axis	
def rot_x(alpha):
	Rx = np.array([
	[1.0 ,  0.0 , 0.0 , 0.0],
	[0.0 , math.cos(alpha) , -math.sin(alpha) , 0.0],
	[0.0 , math.sin(alpha) , math.cos(alpha) , 0.0],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		
	return Rx
	
# basic transformation for rotation about y axis	
def rot_y(beta):
	Ry = np.array([
	[math.cos(beta) ,  0.0 , math.sin(beta) , 0.0],
	[0.0 , 1.0 , 0.0 , 0.0],
	[-math.sin(beta) , 0.0 , math.cos(beta) , 0.0],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		
	return Ry
	
# basic transformation for rotation about z axis	
def rot_z(gamma):
	Rz = np.array([
	[math.cos(gamma) ,  -math.sin(gamma) , 0.0 , 0.0],
	[math.sin(gamma) ,   math.cos(gamma) , 0.0 , 0.0],
	[0.0 , 0.0 , 1.0 , 0.0],
	[0.0 , 0.0 , 0.0 , 1.0]
	])
		
	return Rz
	
	
