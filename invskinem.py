# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math as m
def invskinem(pose=[0,0,0]):
     L1=115
     L2=64
     a1=18
     d1=pose[2]
     c3=((pose[0]-a1)**2+pose[1]**2-L1**2-L2**2)/(2*L1*L2)
     s3=-m.sqrt(1-c3**2)
     th3=m.atan2(s3,c3)
     k=((pose[0]-a1)**2+L1**2+pose[1]**2-L2**2)/(2*L1)
     th2=m.atan2(-m.sqrt((pose[0]-a1)**2+pose[1]**2-k**2),k)+m.atan2(pose[1],pose[0]-a1)
     return [d1,th2,th3]
     
     
