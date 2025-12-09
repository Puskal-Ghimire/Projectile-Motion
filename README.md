# Projectile Motion Simulation (Web VPython 3.2)

This repository contains a Web VPython program that simulates the 2D motion of a projectile under gravity. The simulation visualizes the projectile’s trajectory, velocity vector, speed, and calculates important physical quantities such as time of flight and horizontal range.

## Features

* User input for initial velocity and angle of projection
* Real-time projectile animation using Web VPython
* Live speed label above the projectile
* Ground plane and motion trail
* Displays total time of flight
* Displays horizontal range at the end of the simulation

## Physics Used

The simulation uses standard projectile motion equations:

* Horizontal velocity:
  vx = v0 * cos(theta)

* Vertical velocity:
  vy = v0 * sin(theta) - g * t

* Horizontal position:
  x = x0 + vx * t

* Vertical position:
  y = v0 * sin(theta) * t - 0.5 * g * t^2

Gravity is taken as g = 9.8 m/s².

## How to Run

1. Open Web VPython (GlowScript):
   https://www.glowscript.org

2. Create a new program.

3. Copy and paste the code from this repository into the editor.

4. Run the program.

5. Enter:

   * Initial velocity (m/s)
   * Angle of projection (degrees)

The simulation will animate the projectile motion and display the calculated results.

## Project Structure

```
projectile-motion/
│
├── projectile.py           # Web VPython code
└── README.md               # Project documentation
```
