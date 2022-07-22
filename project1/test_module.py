def calculate(list):
  #check input
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  #import numpy 
  import numpy as np
  #convert list to 3x3 numpy array
  num = np.reshape(list,[3,3])
  #create dictionary
  calculations=dict()
  #calculate mean
  ans_mean = [np.mean(num,axis=0).tolist(),np.mean(num,axis=1).tolist(),  np.mean(num).tolist()]
  calculations['mean'] = ans_mean
  #calculate variance
  ans_var = [np.var(num,axis=0).tolist(),np.var(num,axis=1).tolist(),np.var(num).tolist()]
  calculations['variance'] = ans_var
 #calculate standard deviation
  ans_std = [np.std(num,axis=0).tolist(),np.std(num,axis=1).tolist(),np.std(num).tolist()]
  calculations['standard deviation'] = ans_std
  #show max
  ans_max = [np.max(num,axis=0).tolist(),np.max(num,axis=1).tolist(),np.max(num).tolist()]
  calculations['max'] = ans_max
  #show min
  ans_min = [np.min(num,axis=0).tolist(),np.min(num,axis=1).tolist(),np.min(num).tolist()]
  calculations['min'] = ans_min
  #show sum
  ans_sum = [np.sum(num,axis=0).tolist(),np.sum(num,axis=1).tolist(),np.sum(num).tolist()]
  calculations['sum'] = ans_sum
  return calculations
