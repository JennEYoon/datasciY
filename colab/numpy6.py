# quick test, vs code setup 
# 6/21/2022
# Remote extension pack installed, can access files on wsl$  
# Select python interpreter, conda envs on wsl$ available.  
#
# Change default interpreter - conda env 'base' on wsl2 set as default.  
#
# To change interpreter, first close all open terminals, then Control+Shift+P 
# and change python interpreter. New terminal with new conda env activated opens. 
# Shift+Enter runs python lines on the new terminal with new conda env.    

import numpy as np
x = np.arange(10)
print(x*2)
print(np.__version__)

# Success, did run on selected python interpreter on wsl.  
# How to set default?  
print(x+3)

import sys
path = sys.executable
print(path)
# shows new env path: /home/jyoon/conda3/envs/dl37/bin/python
# for python v3.7, pytorch gpu, fastai.  