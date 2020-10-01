"""
    Code by Tae-Hwan Hung(@graykode)
    https://www.geeksforgeeks.org/python-uniform-distribution-in-statistics/
"""
# importing library 
  
from scipy.stats import uniform  
    
numargs = uniform .numargs  
a, b = 0.2, 0.8
rv = uniform (a, b)  
    
print ("RV : \n", rv)
