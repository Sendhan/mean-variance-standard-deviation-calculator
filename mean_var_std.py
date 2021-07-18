import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  nparray = np.array(list).reshape(3,3)

  calculations = {
    "mean": [
      np.mean(nparray, axis = 0).tolist(),
      np.mean(nparray, axis = 1).tolist(),
      np.mean(nparray.tolist())
    ],
    "variance": [
      np.var(nparray, axis = 0).tolist(),
      np.var(nparray, axis = 1).tolist(),
      np.var(nparray) .tolist()    
    ],
    "standard deviation": [
      np.std(nparray, axis = 0).tolist(),
      np.std(nparray, axis = 1).tolist(),
      np.std(nparray).tolist()     
    ],   
    "max": [
      np.max(nparray, axis = 0).tolist(),
      np.max(nparray, axis = 1).tolist(),
      np.max(nparray).tolist()     
    ], 
    "min": [
      np.min(nparray, axis = 0).tolist(),
      np.min(nparray, axis = 1).tolist(),
      np.min(nparray).tolist()     
    ], 
    "sum": [
      np.sum(nparray, axis = 0).tolist(),
      np.sum(nparray, axis = 1).tolist(),
      np.sum(nparray).tolist()     
    ],  
  }


  return calculations