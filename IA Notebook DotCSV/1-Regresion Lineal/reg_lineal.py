
# coding: utf-8

# In[2]:


import numpy as np
import scipy as sc # como numpy pero mas completo, img, datos, etc

import matplotlib.pyplot as plt # graficar


# In[3]:


# se trabajara con un dataset ya implementado, load_boston
from sklearn.datasets import load_boston


# In[5]:


boston = load_boston()
#print boston.DESCR


# error cuadratico medio: $\beta = (X^{T}X)^{-1}X^{T}Y$

# In[79]:


# usaremos el numero medio de habitaciones para predecir su valor medio (viviendas)
X = np.array(boston.data[:,5]) # num med habit 
Y = np.array(boston.target) # valor med miles dlls
plt.scatter(X,Y,alpha=0.4)
plt.show()

# la idea es encontrar la recta que permita predecir el valor medio segun el num de habitaciones

# añadimos columna de 1 para los terminos independientes
X = np.array([np.ones(506),X]).T

B = np.linalg.inv(X.T @ X) @ X.T @ Y


# In[ ]:


# dibujar la linea

plt.plot([4,9,[b[0]+b[1]*4],b[0]+b[1]*9],c="red")
plt.show()

