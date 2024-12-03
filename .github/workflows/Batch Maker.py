import math
n = 6  # Number of elements in the alloy system (Re, Cr, V, Ti, Ta, W)
delta_x = 0.1  # Mole fraction interval
k = int(1 / delta_x)  # k represents the number of possible divisions from 0 to 1 (inclusive)
# N_combinations = (k + n - 1) choose (n - 1)
N_combinations_0_1 = math.comb(k + n - 1, n - 1)
N_combinations_0_1

