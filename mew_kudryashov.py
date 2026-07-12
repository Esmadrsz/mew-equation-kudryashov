# Analytical solution of the MEW equation via the Modified Kudryashov Method
# Esma Dogrusozlu, 2026
#
# MEW equation: u_t + 3*alpha*u^2*u_x - beta*u_xxt = 0
# Traveling wave transformation: u(x,t) = U(xi), xi = x - c*t
# Solution: U(xi) = a0 * tanh( (ln(a)/2)*xi + (1/2)*ln(d) )

import numpy as np
import matplotlib.pyplot as plt


def mew_solution(x, t, a0=1.0, a=2.0, d=1.0, c=1.0):
    # kink-type soliton solution
    xi = x - c * t
    return a0 * np.tanh((np.log(a) / 2) * xi + (1 / 2) * np.log(d))


def plot_wave_profiles(x):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("MEW Equation – Kink Soliton Solution (Modified Kudryashov Method)",
                 fontsize=13)

    # vary amplitude
    ax = axes[0]
    for a0 in [0.5, 1.0, 1.5, 2.0]:
        U = mew_solution(x, t=0, a0=a0, a=2.0, d=1.0, c=1.0)
        ax.plot(x, U, label=f"a0 = {a0}")
    ax.set_title("Effect of amplitude parameter")
    ax.set_xlabel("x")
    ax.set_ylabel("U(x, 0)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', linewidth=0.5)

    # vary transition width
    ax = axes[1]
    for a in [1.5, 2.0, 3.0, 5.0]:
        U = mew_solution(x, t=0, a0=1.0, a=a, d=1.0, c=1.0)
        ax.plot(x, U, label=f"a = {a}")
    ax.set_title("Effect of transition width parameter")
    ax.set_xlabel("x")
    ax.set_ylabel("U(x, 0)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', linewidth=0.5)

    plt.tight_layout()
    plt.savefig("wave_profiles.png", dpi=150, bbox_inches='tight')
    plt.show()


def plot_propagation(x, t_values):
    fig, ax = plt.subplots(figsize=(10, 6))
    cmap = plt.cm.viridis
    colors = cmap(np.linspace(0, 1, len(t_values)))

    for t, color in zip(t_values, colors):
        U = mew_solution(x, t, a0=1.0, a=2.0, d=1.0, c=0.5)
        ax.plot(x, U, color=color, label=f"t = {t:.1f}")

    ax.set_title("Wave Propagation – Kink Soliton Preserves Shape Over Time", fontsize=12)
    ax.set_xlabel("x")
    ax.set_ylabel("U(x, t)")
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

    sm = plt.cm.ScalarMappable(cmap=cmap,
                                norm=plt.Normalize(vmin=t_values[0], vmax=t_values[-1]))
    sm.set_array([])
    plt.colorbar(sm, ax=ax, label='Time t')

    plt.tight_layout()
    plt.savefig("wave_propagation.png", dpi=150, bbox_inches='tight')
    plt.show()


def print_parameters():
    a0, a, c = 1.0, 2.0, 1.0
    alpha = c / a0**2
    beta = np.sqrt(2) / abs(np.log(a))
    print("Parameter relations from the algebraic system:")
    print(f"  alpha = c / a0^2 = {alpha:.4f}")
    print(f"  beta  = sqrt(2) / |ln(a)| = {beta:.4f}")
    print(f"  a1    = -2 * a0 = {-2*a0}")


if __name__ == "__main__":
    x = np.linspace(-10, 10, 1000)
    t_values = np.linspace(0, 4, 9)

    print_parameters()
    plot_wave_profiles(x)
    plot_propagation(x, t_values)
