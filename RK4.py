import matplotlib.pyplot as plt

def acceleration(x, y):
    r = (x**2 + y**2)**0.5
    return -x/r**3, -y/r**3


def rk4_step(x, y, vx, vy, dt):

    #K1
    ax1, ay1 = acceleration(x, y)
    k1x = vx
    k1y = vy
    k1vx = ax1
    k1vy = ay1

    #K2
    ax2, ay2 = acceleration(
        x + 0.5*dt*k1x,
        y + 0.5*dt*k1y
    )
    k2x = vx + 0.5*dt*k1vx
    k2y = vy + 0.5*dt*k1vy
    k2vx = ax2
    k2vy = ay2

    #K3
    ax3, ay3 = acceleration(
        x + 0.5*dt*k2x,
        y + 0.5*dt*k2y
    )
    k3x = vx + 0.5*dt*k2vx
    k3y = vy + 0.5*dt*k2vy
    k3vx = ax3
    k3vy = ay3

    #K4
    ax4, ay4 = acceleration(
        x + dt*k3x,
        y + dt*k3y
    )
    k4x = vx + dt*k3vx
    k4y = vy + dt*k3vy
    k4vx = ax4
    k4vy = ay4

    #FINAL UPDATE
    x_new = x + dt/6 * (k1x + 2*k2x + 2*k3x + k4x)
    y_new = y + dt/6 * (k1y + 2*k2y + 2*k3y + k4y)

    vx_new = vx + dt/6 * (k1vx + 2*k2vx + 2*k3vx + k4vx)
    vy_new = vy + dt/6 * (k1vy + 2*k2vy + 2*k3vy + k4vy)

    return x_new, y_new, vx_new, vy_new


#SIMULATION

x = 1.0
y = 0.0
vx = 0.0
vy = 1.0

dt = 0.0001
N = 100000

x_values = [x]
y_values = [y]
energy_values = []

for i in range(N):

    x, y, vx, vy = rk4_step(x, y, vx, vy, dt)

    x_values.append(x)
    y_values.append(y)

    r = (x**2 + y**2)**0.5
    energy = 0.5 * (vx**2 + vy**2) - 1/r
    energy_values.append(energy)

#ORBIT PLOT

plt.plot(x_values, y_values)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbite — RK4")
plt.show()

#ENERGY PLOT

plt.plot(energy_values)
plt.xlabel("Nombre de pas")
plt.ylabel("Énergie")
plt.title("Énergie — RK4")
plt.show()

max_error = max(abs(E + 0.5) for E in energy_values)

print("Erreur énergétique maximale :", max_error)