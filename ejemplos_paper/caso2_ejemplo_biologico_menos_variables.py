import numpy as np

from a_revisar.examples.barvinok_examples import run_barvinok

M = np.array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0, 2, 0,  0,  0,  0, -2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, 0,  0,  0,  0,  1],
       [ 0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  2],
       [ 0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  1],
       [ 0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  1],
       [ 0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0, -1],
       [ 0,  0,  0,  0,  0, -2, -2,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0,  1],
       [ 0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0,  0,  0, -2],
       [ 0,  0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, 0,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0, -1,  0,  0,  0],
       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1, 0,  0, -1,  0,  0]])

n = 17
m = 2
#cProfile.run('run_barvinok(M, n, m)', 'restats')
run_barvinok(M, n, m)

#borrar if i > 1000 break

