import numpy as np
import math

def cosine_similarity(v1, v2):
	s1 = 0
	s2 = 0
	for i in range(len(v1)):
		s1 += v1[i]**2
		s2 += v2[i]**2
	
	s1 **= 0.5
	s2 **= 0.5

	return round(dot(v1, v2)/(s1 * s2), 3)

def dot(v1, v2):
	d = 0
	for i in range(len(v1)):
		d += v1[i]*v2[i]
	return d
