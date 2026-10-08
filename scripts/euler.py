import matplotlib.pyplot as plt
import numpy as np

def acceleration(x, y):
    r = ((x**2 + y**2)**0.5)
    ax = -x/(r**3)
    ay = -y/(r**3)
    return ax, ay

print(acceleration(1, 0)
)

x = 1.0
y = 0.0
vx = 0.0
vy = 1.0
dt = 0.001

x_values = [x]
y_values = [y]
energy_values = []

#CALCULATION OF ORBIT USING EULER METHOD

for i in range(10000):
    ax, ay = acceleration(x, y)

    vx_new = vx + ax * dt
    vy_new = vy + ay * dt

    x_new = x + vx * dt
    y_new = y + vy * dt

    x = x_new
    y = y_new
    vx = vx_new
    vy = vy_new

    x_values.append(x)
    y_values.append(y)

    r = (x**2 + y**2)**0.5
    energy = 0.5 * (vx**2 + vy**2) - 1/r
    
    energy_values.append(energy)


#PLOT OF ENERGY EVOLUTION

plt.plot(energy_values)

plt.xlabel("Nombre de pas")
plt.ylabel("Énergie")
plt.title("Évolution de l'énergie — méthode d'Euler")

plt.show()

r_final = (x**2 + y**2)**0.5

print("Position finale :", x, y)
print("Distance finale au Soleil :", r_final)


#VISUAL PLOT FOR ORBIT COMPARISON

theta = np.linspace(0, 2*np.pi, 500)

x_exact = np.cos(theta)
y_exact = np.sin(theta)

plt.plot(x_exact, y_exact, label="Orbite exacte")
plt.plot(x_values, y_values, label="Euler")

plt.plot(x_values, y_values)

plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

plt.show()
