#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Make a 2D FDTD simulation and animate the result. The walls are
perfectly conducting, and in the center of the domain is a dielectric
inclusion.

The polarization is (Ez,Hx,Hy), with simulation in the xy-plane. The
staggered grid is implemented as

Ez[0,0] -- Hy[0,0] -- Ez[1,0] -- Hy[1,0] --
   |          |          |          |
Hx[0,0] ------|------ Hx[1,0] ------|------
   |          |          |          |
Ez[0,1] -- Hy[0,1] -- Ez[1,1] -- Hy[1,1] --
   |          |          |          |
Hx[0,1] ------|------ Hx[1,1] ------|------
   |          |          |          |
Ez[0,2] -- Hy[0,1] -- Ez[1,2] -- Hy[1,2] --
   |          |          |          |

Daniel Sjoberg, 2013-09-15
"""

import matplotlib
matplotlib.interactive(True)

from pylab import *

# Some natural constants to set units
c0 = 299792458.        # Speed of light in vacuum
mu0 = 4*pi*1e-7        # Permeability of vacuum
eps0 = 1/c0**2/mu0     # Permittivity of vacuum
eta0 = sqrt(mu0/eps0)  # Wave impedance of vacuum

# Simulation parameters
f0 = 1e9               # Center frequency of wave
lambda0 = c0/f0        # Center wavelength
N_per_wavelength = 15  # Number of points per wavelength
dx = lambda0/N_per_wavelength
dy = lambda0/N_per_wavelength
dt = 1/sqrt(1/dx**2 + 1/dy**2)/c0*0.9
Lx = 7.                # Dimension of simulation domain in the x direction
Ly = 7.                # Dimension of simulation domain in the y direction
x = arange(0, Lx, dx)
y = arange(0, Ly, dy)
Nx = len(x)            # Number of points in the x direction
Ny = len(y)            # Number of points in the y direction
Ez = zeros((Nx, Ny))   # Set up values of Ez, Hx, Hy, note the staggered
Hx = zeros((Nx, Ny-1)) # grid (less values in some directions)
Hy = zeros((Nx-1, Ny))
Jz0 = zeros((Nx, Ny))  # Spatial distribution of the excitation
J0_idx_x = int(Nx/4)   # The current is non-zero only in one point
J0_idx_y = int(Ny/3)
Jz0[J0_idx_x,J0_idx_y] = 1.

t_stop = sqrt(Lx**2 + Ly**2)/c0*3  # Estimated stop time
tvec = arange(0, t_stop, dt)       # Vector of time values
epsilon = ones((Nx, Ny))           # Array of relative permittivity values
epsr = 4.                          # Permittivity of center square
Dx = Lx/5                          # Set size of center square
Dy = Ly/5
for nx in range(0, Nx):
    for ny in range(0, Ny):
        if (x[nx]>Lx/2-Dx/2) and (x[nx]<Lx/2+Dx/2) and \
                (y[ny]>Ly/2-Dy/2) and (y[ny]<Ly/2+Dy/2):
            epsilon[nx,ny] = epsr

def J0(t):
    """
    Return the input current at time t.
    """
    w = lambda0/c0     # Width of pulse
    t0 = w             # Delay of pulse
    omega0 = 2*pi*f0   # Center angular frequency
    f = exp(-((t-t0)/(2*w))**2)*cos(omega0*(t-t0))
    return(f)

# Prepare the plotting
fig = figure()        # Create a figure
scale = 0.1           # Typical scale of wave (higher values are clipped)
s = imshow(Ez, vmin=-scale, vmax=scale, cmap='RdBu')
gca().axes.get_xaxis().set_ticks([])  # Turn off x axis ticks
gca().axes.get_yaxis().set_ticks([])  # Turn off y axis ticks

# Do the simulation and plotting in an infinite loop
while True:
    # Initiate the field values before each time sequence
    Ez = zeros((Nx, Ny))
    Hx = zeros((Nx, Ny-1))
    Hy = zeros((Nx-1, Ny))
    for t in tvec:                            # Loop through the time values
        rotE_x = (Ez[:,1:] - Ez[:,:-1])/dy    # x component of rot(E)
        rotE_y = -(Ez[1:,:] - Ez[:-1,:])/dx   # y component of rot(E)
        Hx[:,:] = Hx[:,:] - 1/mu0*dt*rotE_x   # Update Hx
        Hy[:,:] = Hy[:,:] - 1/mu0*dt*rotE_y   # Update Hy
        rotH_z = (Hy[1:,1:-1] - Hy[:-1,1:-1])/dx - \
            (Hx[1:-1,1:] - Hx[1:-1,:-1])/dy   # z component of rot(H)
        # Update Ez. Note that the boundary values are not updated
        # since the wall is perfectly conducting (Ez=0)
        Ez[1:-1,1:-1] = Ez[1:-1,1:-1] + \
            1/eps0/epsilon[1:-1,1:-1]*dt*(rotH_z - Jz0[1:-1,1:-1]*J0(t))
        s.set_data(Ez)                        # Update data in the plot
        draw()                                # Redraw the plot