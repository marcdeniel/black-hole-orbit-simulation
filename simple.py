import numpy as np
#constants
G = 6.67430e-11 #gravational constant cubic meters per kg per second squared (m^3 kg^-1 s^-2)
c = 3.0e8 #speed of light m/s in a vacuum
M = 1.989e30 #1 solar mass of the black hole

#schwarzschild radius *event horizon*
r_s = 2*G*M/ c**2

#initial
r0 = 10 * r_s  
theta0 = 0    
phi0 = 0      
vr0 = 0        
vtheta0 = 0   
vphi0 = np.sqrt(G * M / r0)  


dt = 1        
t_total = 1000 
times = np.arange(0, t_total, dt)

r = r0
phi = phi0

r_positions = []
phi_positions = []


for t in times:
    r += vr0 * dt
    phi += vphi0 * dt / r
    
  
    r_positions.append(r)
    phi_positions.append(phi)

x_positions = np.array(r_positions) * np.cos(phi_positions)
y_positions = np.array(r_positions) * np.sin(phi_positions)
