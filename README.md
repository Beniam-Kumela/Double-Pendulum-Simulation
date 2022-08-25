# Double-Pendulum-Simulation
This simulation used physics to simulate the two dimensional motion of a double pendulum. 

The following formulas below to calculate angular acceleration of rod 1 and rod 2:

<img width="590" alt="image" src="https://user-images.githubusercontent.com/106757076/186555717-f62751b5-171c-47cf-9a6c-721ea9dc7dd9.png">

were taken from the website, https://www.myphysicslab.com/pendulum/double-pendulum-en.html, which explains the physics of the simulation in detail.

The python module pygame was explored, particular how to use vectors and geometry to calculate object position as well as learning how to implement such physics into the modules interface while maintaining consistency and smoothness in fps.

Euler's method was applied to the angular acceleration formulas in combination with simple trigonometry were used to track the position of both masses.

Below are some examples of mass and angle combinations modeled:

Mass 1 = 100g, Mass 2 = 10g, Angle of rod 1 = pi/3, Angle of rod 2 = pi/4

![ezgif-2-949f636913](https://user-images.githubusercontent.com/106757076/186556147-fd696bf5-85f7-431c-b727-d7db55f7399a.gif)

Mass 1 = 100g, Mass 2 = 100g, Angle of rod 1 = pi/4, Angle of rod 2 = pi/8

![ezgif-2-a7fafe1ab8](https://user-images.githubusercontent.com/106757076/186556764-d8d31016-c44a-4511-9696-2cc85500bbde.gif)

You can download the python script and play around with the variable rod lengths, angles, masses, and even gravity to get some cool simulations. 
