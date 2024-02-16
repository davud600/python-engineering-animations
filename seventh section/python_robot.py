import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 1
dt = 0.005
t = np.arange(0, t_end+dt, dt)


# Joint 1
r1 = 3 + t
f1 = 1
alpha1 = 2*np.pi*f1*t
x1 = (r1)*np.cos(alpha1)
y1 = (r1)*np.sin(alpha1)

# Joint 2
r2 = 3 + t
f2 = 1
alpha2 = 2*np.pi*f2*t
dx1 = (r2)*np.cos(alpha2+alpha1)
dy1 = (r2)*np.sin(alpha2+alpha1)
x2 = x1 + dx1
y2 = y1 + dy1

############### Animation ###############
frame_amount = len(t)


def update_plot(num):
    return


fig = plt.figure(figsize=(16, 9), dpi=80, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 3)

# Subplot 1
ax1 = fig.add_subplot(gs[:, 0:2], facecolor=(0.9, 0.9, 0.9))
base_line, = ax1.plot([0, 0], [0, 0.4], 'k', linewidth=20)
joint_1, = ax1.plot([], [], 'k', linewidth=4)
joint_2, = ax1.plot([], [], 'b', linewidth=4)
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position(('center'))
ax1.xaxis.set_label_coords(0.5, -0.01)
ax1.yaxis.set_label_coords(-0.002, 0.5)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(np.arange(-10, 10+1, 1))
plt.yticks(np.arange(-10, 10+1, 1))
plt.xlabel('meters [m]', fontsize=12)
plt.ylabel('meters [m]', fontsize=12)


# ani = animation.FuncAnimation(
#     fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
