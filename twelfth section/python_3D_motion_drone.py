# https://www.udemy.com/certificate/UC-b5a6e33c-1d0d-42ec-ada1-3a8a5c5e2847/

'''
LICENSE AGREEMENT
In relation to this Python file:
1. Copyright of this Python file is owned by the author: Mark Misin
2. This Python code can be freely used and distributed
3. The copyright label in this Python file such as
copyright=ax_main.text(x,y,'© Mark Misin Engineering',size=z)
that indicate that the Copyright is owned by Mark Misin MUST NOT be removed.

WARRANTY DISCLAIMER!
This Python file comes with absolutely NO WARRANTY! 
In no event can the author of this Python file be held responsible
for whatever happens in relation to this Python file.
For example, if there is a bug in the code and because of that a project,
invention, or whatever it is used for fails - the author is NOT RESPONSIBLE!
'''

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Create the time array
t0 = 0
t_end = 10
dt = 0.02
t = np.arange(t0, t_end+dt, dt)

# Create array for x & y dimensions
r = 0.5+0*t
f = 0.25+0*t
x = 0*t
y = 0*t

# Create array for the  Z dimension
z = t

############################## ANIMATION ###########################
frame_amount = len(t)


def update_plot(num):
    # Trajectory
    # plane_trajectory.set_data(x[0:num],y[0:num])
    plane_trajectory.set_xdata(x[0:num])
    plane_trajectory.set_ydata(y[0:num])
    plane_trajectory.set_3d_properties(z[0:num])

    pos_x.set_data(t[0:num], x[0:num])
    pos_y.set_data(t[0:num], y[0:num])
    pos_z.set_data(t[0:num], z[0:num])

    drone_body_x.set_xdata([x[num]-r[num], x[num]+r[num]])
    drone_body_x.set_ydata([y[num], y[num]])

    drone_body_y.set_xdata([x[num], x[num]])
    drone_body_y.set_ydata([y[num]-r[num], y[num]+r[num]])

    if matplotlib.__version__ == "3.1.3" or matplotlib.__version__ == "3.2.0rc3" or matplotlib.__version__ == "3.2.0" or matplotlib.__version__ == "3.2.1" or matplotlib.__version__ == "3.2.2":
        drone_body_x.set_3d_properties([z[num], z[num]])
        drone_body_y.set_3d_properties([z[num], z[num]])

    drone_body_x.set_xdata(
        [x[num]-r[num]*np.cos(np.pi/6), x[num]+r[num]*np.cos(np.pi/6)])
    drone_body_x.set_ydata([y[num], y[num]])

    drone_body_y.set_xdata([x[num], x[num]])
    drone_body_y.set_ydata([y[num]-r[num], y[num]+r[num]])

    if matplotlib.__version__ == "3.1.3" or matplotlib.__version__ == "3.2.0rc3" or matplotlib.__version__ == "3.2.0" or matplotlib.__version__ == "3.2.1" or matplotlib.__version__ == "3.2.2":
        drone_body_x.set_3d_properties(
            [z[num]+r[num]*np.sin(np.pi/6), z[num]-r[num]*np.sin(np.pi/6)])
        drone_body_y.set_3d_properties([z[num], z[num]])

    drone_body_x.set_xdata([x[num]-r[num], x[num]+r[num]])
    drone_body_x.set_ydata([y[num], y[num]])

    drone_body_y.set_xdata([x[num], x[num]])
    drone_body_y.set_ydata(
        [y[num]-r[num]*np.cos(np.pi/6), y[num]+r[num]*np.cos(np.pi/6)])

    if matplotlib.__version__ == "3.1.3" or matplotlib.__version__ == "3.2.0rc3" or matplotlib.__version__ == "3.2.0" or matplotlib.__version__ == "3.2.1" or matplotlib.__version__ == "3.2.2":
        drone_body_x.set_3d_properties([z[num], z[num]])
        drone_body_y.set_3d_properties(
            [z[num]-r[num]*np.sin(np.pi/6), z[num]+r[num]*np.sin(np.pi/6)])

    drone_body_x.set_xdata([x[num]-r[num]*np.cos(2*np.pi*(f[num])*t[num]),
                           x[num]+r[num]*np.cos(2*np.pi*(f[num])*t[num])])
    drone_body_x.set_ydata([y[num]-r[num]*np.sin(2*np.pi*(f[num])*t[num]),
                           y[num]+r[num]*np.sin(2*np.pi*(f[num])*t[num])])

    drone_body_y.set_xdata([x[num]-r[num]*np.cos(2*np.pi*(f[num])*t[num]+np.pi/2),
                           x[num]+r[num]*np.cos(2*np.pi*(f[num])*t[num]+np.pi/2)])
    drone_body_y.set_ydata([y[num]-r[num]*np.sin(2*np.pi*(f[num])*t[num]+np.pi/2),
                           y[num]+r[num]*np.sin(2*np.pi*(f[num])*t[num]+np.pi/2)])

    drone_body_x.set_3d_properties([z[num], z[num]])
    drone_body_y.set_3d_properties([z[num], z[num]])

    return plane_trajectory, pos_x, pos_y, pos_z, drone_body_x, drone_body_y


# Set up your figure properties
fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 4)

# 3D motion
ax0 = fig.add_subplot(gs[:, 0:3], projection='3d', facecolor=(0.9, 0.9, 0.9))
ax0.set_title('© Mark Misin Engineering', fontsize=15)
plane_trajectory, = ax0.plot([], [], [], 'r', linewidth=1)
drone_body_x, = ax0.plot([], [], [], 'b', linewidth=5, label='drone_x')
drone_body_y, = ax0.plot([], [], [], 'g', linewidth=5, label='drone_y')
ax0.set_xlim(-3, 3)
ax0.set_ylim(-3, 3)
ax0.set_zlim(min(z), max(z))
# ax0.set_xticks([0])
# ax0.set_yticks([0])
# ax0.set_zticks([5])
ax0.set_xlabel('position_x [m]', fontsize=12)
ax0.set_ylabel('position_y [m]', fontsize=12)
ax0.set_zlabel('position_z [m]', fontsize=12)
plt.grid(True)

ax1 = fig.add_subplot(gs[0, 3], facecolor=(0.9, 0.9, 0.9))
pos_x, = ax1.plot([], [], 'b', linewidth=1)
plt.xlim(t0, t_end)
plt.ylim(-3, 3)
plt.ylabel('position_x [m]', fontsize=12)
plt.grid(True)

ax2 = fig.add_subplot(gs[1, 3], facecolor=(0.9, 0.9, 0.9))
pos_y, = ax2.plot([], [], 'b', linewidth=1)
plt.xlim(t0, t_end)
plt.ylim(-3, 3)
plt.ylabel('position_y [m]', fontsize=12)
plt.grid(True)

ax3 = fig.add_subplot(gs[2, 3], facecolor=(0.9, 0.9, 0.9))
pos_z, = ax3.plot([], [], 'b', linewidth=1)
plt.xlim(t0, t_end)
plt.ylim(min(z), max(z))
plt.xlabel('time [s]', fontsize=12)
plt.ylabel('position_z [m]', fontsize=12)
plt.grid(True)

plane_ani = animation.FuncAnimation(fig, update_plot,
                                    frames=frame_amount, interval=20, repeat=False, blit=True)
plt.show()


###########################
