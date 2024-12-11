import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import expon
from scipy.stats import norm
from matplotlib.animation import FuncAnimation

lambda_exp = 1.0  # parametr lambda rozkładu wykładniczego
R = 10000  # liczba symulacji
Ns = [2, 3, 10, 50, 100, 10000]  # liczba próbek

HIST_BINS = np.linspace(-3, 3, 100)

fig, ax = plt.subplots()
ax.set_ylim(top = 0.5)
ax.set_xticks(np.linspace(-3,3,31))
ax.grid(True, which='major', linestyle='--', color='black', alpha=0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

x_axis = np.arange(-3, 3, 0.1)
ax.plot(x_axis, norm.pdf(x_axis, 0, 1), color='#d81111', linewidth=2)

_, _, bars = ax.hist([], HIST_BINS, color='#3397c9')

def animate(i):
    N = Ns[i]

    Us = np.zeros(R)

    for r in range(R):
        X = expon.rvs(scale=1. / lambda_exp, size=N)
        Us[r] = (np.sum(X)/N - 1./lambda_exp) * np.sqrt(N) * lambda_exp

    heights, _ = np.histogram(Us, bins=HIST_BINS, density=True)

    for height, bar in zip(heights, bars.patches):
        bar.set_height(height)

    ax.set_title(f'Wizualizacja CTG dla\n{N=}', fontweight="bold", size=16)

    return bars.patches

anim = FuncAnimation(fig, animate, blit = True, frames=len(Ns), interval=500)
anim.save('CTGdlaExpon.gif',writer='pillow')
