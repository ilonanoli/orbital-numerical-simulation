import matplotlib.pyplot as plt

def acceleration(x, y):
    r = (x**2 + y**2)**0.5
    ax = -x / r**3
    ay = -y / r**3
    return ax, ay


x = 1.0
y = 0.0
vx = 0.0
vy = 1.0

dt = 0.001
N = 10000

x_values = [x]
y_values = [y]
energy_values = []

for i in range(N):

    ax, ay = acceleration(x, y)

    x_new = x + vx * dt + 0.5 * ax * dt**2
    y_new = y + vy * dt + 0.5 * ay * dt**2

    ax_new, ay_new = acceleration(x_new, y_new)

    vx_new = vx + 0.5 * (ax + ax_new) * dt
    vy_new = vy + 0.5 * (ay + ay_new) * dt

    x = x_new
    y = y_new
    vx = vx_new
    vy = vy_new

    x_values.append(x)
    y_values.append(y)

    r = (x**2 + y**2)**0.5
    energy = 0.5 * (vx**2 + vy**2) - 1/r

    energy_values.append(energy)


#ORBIT PLOT

plt.figure()
plt.plot(x_values, y_values)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbite avec Velocity-Verlet")
plt.show()


#ENERGY PLOT

plt.figure()
plt.plot(energy_values)
plt.xlabel("Nombre de pas")
plt.ylabel("Énergie")
plt.title("Conservation de l'énergie — Velocity-Verlet")
plt.show()

max_error = max(abs(E + 0.5) for E in energy_values)

print("Erreur énergétique maximale :", max_error)