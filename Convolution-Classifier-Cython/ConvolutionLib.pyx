import numpy as np

cpdef Normalise(x): #a normalise function just because it will be useful later on
  return x/np.sum(x)

cpdef Convolve(x,ker): #convolution function that sweeps the kernel across the spectrum to apply the filter
  cdef int idx = int(x.shape[0])
  cdef int kdim = int(ker.shape[0])
  conv = np.zeros(idx)
  cdef int i
  cdef int j #these frequently referenced variables and loop counters were type-set using C datatypes to improve performance
  for i in range(idx):
    if i<np.floor(kdim/2) or i>idx-np.ceil(kdim/2):
      conv[i]=0
    else:
      for j in range(kdim):
        conv[i] += ker[j]*x[int((i+j+idx-np.floor(kdim/2))%idx)]
    if conv[i]<0:
      conv[i]=0
  return Normalise(conv) #calling predefined Normalise() function
