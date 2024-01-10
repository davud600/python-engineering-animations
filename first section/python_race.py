import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 2
dt = 0.005

# t (time) array
t = np.arange(t0, t_end+dt, dt)  # [hr]

# Airplane 1

# x array
a1 = 800
n1 = 1
x1 = a1*t**n1  # [km]

# y array
altitude1 = 2.5  # [km]
y1 = np.ones(len(t)) * altitude1

# Speed in the x direction (dx/dt)
if n1 < 1:
    t[0] = t[1]
speed_x1 = n1*a1*t**(n1-1)

# Airplane 2

# x array
a2 = 1600/2**0.5
n2 = 0.5
x2 = a2*t**n2  # [km]

# y array
altitude2 = 1.5  # [km]
y2 = np.ones(len(t)) * altitude2

# Speed in the x direction (dx/dt)
if n2 < 1:
    t[0] = t[1]
speed_x2 = n2*a2*t**(n2-1)

# Airplane 3

# x array
a3 = 200
n3 = 3
x3 = a3*t**n3  # [km]

# y array
altitude3 = 0.5  # [km]
y3 = np.ones(len(t)) * altitude3

# Speed in the x direction (dx/dt)
if n3 < 1:
    t[0] = t[1]
speed_x3 = n3*a3*t**(n3-1)

### ANIMATION ###

frame_amount = len(t)

dot1 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i == n:
        dot1[i] = x1[i]
        n += 20
    else:
        dot1[i] = x1[n-20]


dot2 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i == n:
        dot2[i] = x2[i]
        n += 20
    else:
        dot2[i] = x2[n-20]


dot3 = np.zeros(frame_amount)
n = 20
for i in range(0, frame_amount):
    if i == n:
        dot3[i] = x3[i]
        n += 20
    else:
        dot3[i] = x3[n-20]


def update_plot(num):
    # 1st subplot
    plane1_trajectory.set_data(dot1[0:num], y1[0:num])
    plane1_1.set_data([x1[num] - 40, x1[num] + 20], [y1[num], y1[num]])
    plane1_2.set_data([x1[num] - 20, x1[num]], [y1[num] + 0.3, y1[num]])
    plane1_3.set_data([x1[num] - 20, x1[num]], [y1[num] - 0.3, y1[num]])
    plane1_4.set_data([x1[num] - 40, x1[num] - 30], [y1[num] + 0.15, y1[num]])
    plane1_5.set_data([x1[num] - 40, x1[num] - 30], [y1[num] - 0.15, y1[num]])

    plane2_trajectory.set_data(dot2[0:num], y2[0:num])
    plane2_1.set_data([x2[num] - 40, x2[num] + 20], [y2[num], y2[num]])
    plane2_2.set_data([x2[num] - 20, x2[num]], [y2[num] + 0.3, y2[num]])
    plane2_3.set_data([x2[num] - 20, x2[num]], [y2[num] - 0.3, y2[num]])
    plane2_4.set_data([x2[num] - 40, x2[num] - 30], [y2[num] + 0.15, y2[num]])
    plane2_5.set_data([x2[num] - 40, x2[num] - 30], [y2[num] - 0.15, y2[num]])

    plane3_trajectory.set_data(dot3[0:num], y3[0:num])
    plane3_1.set_data([x3[num] - 40, x3[num] + 20], [y3[num], y3[num]])
    plane3_2.set_data([x3[num] - 20, x3[num]], [y3[num] + 0.3, y3[num]])
    plane3_3.set_data([x3[num] - 20, x3[num]], [y3[num] - 0.3, y3[num]])
    plane3_4.set_data([x3[num] - 40, x3[num] - 30], [y3[num] + 0.15, y3[num]])
    plane3_5.set_data([x3[num] - 40, x3[num] - 30], [y3[num] - 0.15, y3[num]])

    # 2nd subplot
    x_dist1.set_data(t[0:num], x1[0:num])
    x_dist2.set_data(t[0:num], x2[0:num])
    x_dist3.set_data(t[0:num], x3[0:num])

    # 3rd subplot
    speed1.set_data(t[0:num], speed_x1[0:num])
    speed2.set_data(t[0:num], speed_x2[0:num])
    speed3.set_data(t[0:num], speed_x3[0:num])

    return plane1_trajectory, plane1_1, plane1_2, plane1_3, plane1_4, plane1_5, x_dist1, speed1, \
        plane2_trajectory, plane2_1, plane2_2, plane2_3, plane2_4, plane2_5, x_dist2, speed2, \
        plane3_trajectory, plane3_1, plane3_2, plane3_3, plane3_4, plane3_5, x_dist3, speed3, \



fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)

# Subplot 1
ax0 = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))

# Airplane 1
plane1_trajectory, = ax0.plot([], [], 'r:o', linewidth=2)
plane1_1, = ax0.plot([], [], 'k', linewidth=10)
plane1_2, = ax0.plot([], [], 'k', linewidth=5)
plane1_3, = ax0.plot([], [], 'k', linewidth=5)
plane1_4, = ax0.plot([], [], 'k', linewidth=3)
plane1_5, = ax0.plot([], [], 'k', linewidth=3)

# Airplane 2
plane2_trajectory, = ax0.plot([], [], 'b:o', linewidth=2)
plane2_1, = ax0.plot([], [], 'k', linewidth=10)
plane2_2, = ax0.plot([], [], 'k', linewidth=5)
plane2_3, = ax0.plot([], [], 'k', linewidth=5)
plane2_4, = ax0.plot([], [], 'k', linewidth=3)
plane2_5, = ax0.plot([], [], 'k', linewidth=3)

# Airplane 3
plane3_trajectory, = ax0.plot([], [], 'g:o', linewidth=2)
plane3_1, = ax0.plot([], [], 'k', linewidth=10)
plane3_2, = ax0.plot([], [], 'k', linewidth=5)
plane3_3, = ax0.plot([], [], 'k', linewidth=5)
plane3_4, = ax0.plot([], [], 'k', linewidth=3)
plane3_5, = ax0.plot([], [], 'k', linewidth=3)

# Subplot properties
plt.xlim(x1[0], x1[-1])
plt.ylim(0, y1[0] + 0.5)
plt.xticks(np.arange(x1[0], x1[-1] + 1, x1[-1]/4), size=15)
plt.yticks(np.arange(0, y1[-1] + 1, y1[-1] / y1[-1]), size=15)
plt.xlabel('x-distance', fontsize=15)
plt.ylabel('y-distance', fontsize=15)
plt.title('Airplane', fontsize=20)
plt.grid(True)

# Subplot 2
ax2 = fig.add_subplot(gs[1, 0], facecolor=(0.9, 0.9, 0.9))
x_dist1, = ax2.plot([], [], '-r', linewidth=3, label='X = ' +
                    str(int(a1)) + '*t^' + str(round(n1, 1)))
x_dist2, = ax2.plot([], [], '-b', linewidth=3, label='X = ' +
                    str(int(a2)) + '*t^' + str(round(n2, 1)))
x_dist3, = ax2.plot([], [], '-g', linewidth=3, label='X = ' +
                    str(int(a3)) + '*t^' + str(round(n3, 1)))
plt.xlim(t[0], t[-1])
plt.ylim(x1[0], x1[-1])
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1] / 4), size=15)
plt.yticks(np.arange(x1[0], x1[-1] + 1, x1[-1] / 4), size=15)
plt.xlabel('time [hrs]', fontsize=15)
plt.ylabel('x-distance [km]', fontsize=15)
plt.title('X-distance VS time', fontsize=15)
plt.grid(True)
plt.legend(loc='upper left', fontsize='x-large')

# Subplot 3
ax3 = fig.add_subplot(gs[1, 1], facecolor=(0.9, 0.9, 0.9))
speed1, = ax3.plot([], [], '-r', linewidth=3, label='dX/dt = ' +
                   str(n1) + '*' + str(a1) + '*t^(' + str(n1-1) + ')')
speed2, = ax3.plot([], [], '-b', linewidth=3, label='dX/dt = ' +
                   str(n2) + '*' + str(a2) + '*t^(' + str(n2-1) + ')')
speed3, = ax3.plot([], [], '-g', linewidth=3, label='dX/dt = ' +
                   str(n3) + '*' + str(a3) + '*t^(' + str(n3-1) + ')')
plt.xlim(t[0], t[-1])
plt.ylim(0, speed_x1[-1] * 2)
plt.xticks(np.arange(t[0], t[-1] + dt, t[-1] / 4), size=15)
plt.yticks(np.arange(speed_x1[0], speed_x1[-1]
           * 2 + 1, speed_x1[-1]*2 / 4), size=15)
plt.xlabel('time [hrs]', fontsize=15)
plt.ylabel('speed [km/hr]', fontsize=15)
plt.title('X-distance VS time', fontsize=15)
plt.grid(True)
plt.legend(loc='upper right', fontsize='x-large')

plane_anim = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
