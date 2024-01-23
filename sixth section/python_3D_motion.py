import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

type = 3

# Set up duration for animation
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(0, t_end+dt, dt)

# array for x y z dimensions
r = t**2
f = 0.2*t
a = t
b = t
x = (t)+(t**2)*np.cos(2*np.pi*(0.2*t)*t)
y = (t)+(t**2)*np.sin(2*np.pi*(0.2*t)*t)
z = t

# straight line
line_x = t
line_y = t
line_z = t

############### Animation ###############

frame_amount = len(t)


def update_plot(num):
    plane_trajectory.set_xdata(x[0:num])
    plane_trajectory.set_ydata(y[0:num])
    plane_trajectory.set_3d_properties(z[0:num])

    # straight line
    straight_line.set_xdata(line_x[0:num])
    straight_line.set_ydata(line_y[0:num])
    straight_line.set_3d_properties(line_z[0:num])

    # graphs
    pos_x.set_data(t[0:num], x[0:num])
    pos_y.set_data(t[0:num], y[0:num])
    pos_z.set_data(t[0:num], z[0:num])

    return straight_line, plane_trajectory, pos_x, pos_y, pos_z


fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 4)

ax0 = fig.add_subplot(gs[:, 0:3], projection='3d', facecolor=(0.9, 0.9, 0.9))
plane_trajectory, = ax0.plot(
    [], [], [], 'r', linewidth=4, label='Flight trajectory')
straight_line, = ax0.plot([], [], [], 'b', linewidth=4)
ax0.set_xlim(min(x), max(x))
ax0.set_ylim(min(y), max(y))
ax0.set_zlim(min(z), max(z))
ax0.set_xlabel('position_x [m]', fontsize=12)
ax0.set_ylabel('position_y [m]', fontsize=12)
ax0.set_zlabel('position_z [m]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left', fontsize='large')

ax1 = fig.add_subplot(gs[0, 3], facecolor=(0.9, 0.9, 0.9))
pos_x, = ax1.plot([], [], 'b', linewidth=2,
                  label='x = r(t) * cos(2π * f(t) * t)')
plt.xlim(t0, t_end)
plt.ylim(min(x), max(x))
plt.ylabel('position_x [m]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left', fontsize='small')

ax2 = fig.add_subplot(gs[1, 3], facecolor=(0.9, 0.9, 0.9))
pos_y, = ax2.plot([], [], 'b', linewidth=2,
                  label='y = r(t) * sin(2π * f(t) * t)')
plt.xlim(t0, t_end)
plt.ylim(min(y), max(y))
plt.ylabel('position_y [m]', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left', fontsize='small')

ax3 = fig.add_subplot(gs[2, 3], facecolor=(0.9, 0.9, 0.9))
pos_z, = ax3.plot([], [], 'b', linewidth=2, label='z = t')
plt.xlim(t0, t_end)
plt.ylim(min(z), max(z))
plt.ylabel('position_z [m]', fontsize=12)
plt.grid(True)
plt.legend(loc='lower right', fontsize='small')

anim = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
