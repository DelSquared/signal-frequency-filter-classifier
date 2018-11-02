import numpy as np

cpdef Normalise(x):
  return x/np.sum(x)

cpdef Convolve(x,ker):
  idx = x.shape[0]
  kdim = ker.shape[0]
  conv = np.zeros(idx)
  cdef int i
  cdef int j
  for i in range(idx):
    if i<np.floor(kdim/2) or i>idx-np.ceil(kdim/2):
      conv[i]=0
    else:
      for j in range(kdim):
        conv[i] += ker[j]*x[int((i+j+idx-np.floor(kdim/2))%idx)]
    if conv[i]<0:
      conv[i]=0
  return Normalise(conv)
