# Orbital Numerical Simulation

Numerical simulation of orbital motion using and comparing three numerical integration methods: **Euler, Velocity-Verlet and fourth-order Runge-Kutta (RK4)**.

This project was developed as a personal project in **computational physics and numerical analysis**, with the aim of studying the accuracy, stability and energy conservation of different numerical methods applied to a gravitational two-body problem.

## Objective

The main objectives of this project are to:

- model the motion of a planet around a fixed Sun using Newtonian gravity;
- implement three numerical integration methods;
- compare their numerical accuracy and stability;
- study the conservation of mechanical energy;
- investigate the effect of the time step on the numerical solution.

## Mathematical Model

The motion of a planet under the gravitational attraction of a fixed Sun is described by Newton's law:

\[
\mathbf{F}=-\frac{GMm}{r^3}\mathbf{r}
\]

and therefore

\[
\mathbf{a}=-\frac{GM}{r^3}\mathbf{r}.
\]

For the simulations, normalized units are used:

\[
G=M=1.
\]

The acceleration therefore becomes

\[
\mathbf{a}=-\frac{\mathbf{r}}{r^3}.
\]

The initial conditions are

\[
\mathbf{r}(0)=(1,0),
\qquad
\mathbf{v}(0)=(0,1).
\]

These initial conditions correspond to a theoretical circular orbit.

## Numerical Methods

Three integration schemes are implemented and compared.

### 1. Euler Method

The Euler method updates the position and velocity according to

\[
\mathbf{v}_{n+1}
=
\mathbf{v}_n+\mathbf{a}_n\Delta t
\]

and

\[
\mathbf{r}_{n+1}
=
\mathbf{r}_n+\mathbf{v}_n\Delta t.
\]

Euler's method is simple to implement but introduces significant numerical errors over time.

### 2. Velocity-Verlet Method

The position is updated using

\[
\mathbf{r}_{n+1}
=
\mathbf{r}_n+
\mathbf{v}_n\Delta t+
\frac{1}{2}\mathbf{a}_n\Delta t^2.
\]

The new acceleration is then calculated and the velocity is updated according to

\[
\mathbf{v}_{n+1}
=
\mathbf{v}_n+
\frac{1}{2}
(\mathbf{a}_n+\mathbf{a}_{n+1})\Delta t.
\]

This method is particularly well suited to orbital problems because of its good long-term stability.

### 3. Fourth-Order Runge-Kutta (RK4)

The classical fourth-order Runge-Kutta method is implemented to obtain a higher-order approximation of the solution.

RK4 is compared with Euler and Velocity-Verlet in terms of orbital trajectory and energy conservation.

## Energy Conservation

The specific mechanical energy of the system is

\[
E=
\frac{1}{2}|\mathbf{v}|^2-\frac{1}{r}.
\]

For the chosen initial conditions,

\[
E_0=-\frac{1}{2}.
\]

Energy conservation is used as one of the main indicators of numerical accuracy.

## Results

The simulations show clear differences between the three numerical methods.

- **Euler:** the orbital trajectory progressively deviates from the theoretical circular orbit, while the numerical energy exhibits a systematic drift.
- **Velocity-Verlet:** the orbit remains very close to the theoretical circular trajectory and the energy stays extremely close to its theoretical value, with small bounded oscillations.
- **RK4:** the method provides very high accuracy, with the orbital trajectory remaining close to the theoretical solution and extremely small energy errors for sufficiently small time steps.

The simulations also illustrate the importance of the choice of the time step \(\Delta t\).

## Project Structure

```text
orbital-numerical-simulation/
│
├── README.md
├── euler.py
├── verlet.py
└── rk4.py
```

Additional results and the written report will be added to the repository.

## Technologies

- **Python**
- Numerical integration
- Computational physics
- Numerical analysis
- Mathematical modelling

## Author

**Ilona Belghachem**

Bachelor of Mathematics  
University of Luxembourg

2026
