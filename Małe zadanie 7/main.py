import numpy as np

Wa = np.linspace(0, 1, 11)
Wb = np.linspace(2, 3, 11)
W = np.array(np.meshgrid(Wa, Wb)).T.reshape(-1, 2)

D = np.array([[1.0, 1.3, 0],
              [2.2, 1.1, 1],
              [2.0, 2.4, 1],
              [1.5, 3.2, 0],
              [3.2, 1.2, 1]])

X = D[:, 0:2]

ans = np.zeros([len(W), 3], dtype=np.float64)

i = 0
for weights in W:
    Pr = 1 / (1 + np.exp(-X.dot(weights)))
    errors = Pr - D[:, 2]
    MSE = np.mean(errors ** 2)
    ans[i][0] = weights[0]
    ans[i][1] = weights[1]
    ans[i][2] = MSE
    i += 1

print(ans)
