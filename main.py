import numpy as np
from scipy.spatial.distance import pdist

def calu_sim(hist1,hist2):

    Vec = np.vstack([hist1,hist2])
    acc_mec = 1 - pdist(Vec,'cosine')
    
    return acc_mec

if __name__ == '__main__':

  hist1 = [1,2,3,4]
  hist2 = [2,4,6,8]
  acc_mec = calu_sim(hist1,hist2)
  print("余弦测试结果 dist = "+str(acc_mec))
