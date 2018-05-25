from client import Predictor
import numpy as np


P = Predictor(host="localhost", port=9000)
for i in range(1,100):
    data = np.random.rand(i,2)
    print P.do(data)


