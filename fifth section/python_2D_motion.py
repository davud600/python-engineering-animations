import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

type = 3

# Set up duration for animation
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(0, t_end+dt, dt)

if type == 1:
    # x array
    x_i = 1000
    a = 200
    x = x_i+a*t

    # y array
    y_i = 2000
    b = -100
    y = y_i+b*t
elif type == 2:
    # x array
    x_i = 1000
    a = 200
    x = x_i+a*t**2

    # y array
    y_i = 1000
    A = 500
    f = 0.1
    y = y_i+A*np.sin(2*np.pi*f*t)
else:
    r = 200
    f = 1/5
    a = 1000+40*t
    b = 500+40*t
    x = (1000+40*t)+(r)*np.cos(2*np.pi*(f)*t)
    y = (500+40*t)+(r)*np.sin(2*np.pi*(f)*t)


############### Animation ###############

frame_amount = len(t)


def update_plot(num):

    # Plane
    plane_1.set_data([x[num] - 40, x[num] + 20], [y[num], y[num]])
    plane_2.set_data([x[num] - 15, x[num] + 10], [y[num], y[num]])
    plane_3.set_data([x[num] - 45, x[num] - 30], [y[num]+80, y[num]])
    plane_4.set_data([x[num] - 55, x[num] - 40], [y[num], y[num]])

    # Trajectory
    plane_trajectory.set_data(x[0:num], y[0:num])

    # Subplots 2 and 3
    pos_x.set_data(t[0:num], x[0:num])
    pos_y.set_data(t[0:num], y[0:num])

    if type != 3:
        arr_1 = ax1.arrow(t[num], x_i, 0, x[num] - x_i, length_includes_head=True,
                          head_width=0.1, head_length=40, color='r', linewidth=4)
        arr_2 = ax2.arrow(t[num], y_i, 0, y[num] - y_i, length_includes_head=True,
                          head_width=0.1, head_length=40, color='b', linewidth=4)
        pos_R_1 = ax0.arrow(0, 0, x_i, y_i, length_includes_head=True,
                            head_width=40, head_length=80, color='g', linewidth=2)
        pos_R_2 = ax0.arrow(0, 0, x[num], y[num], length_includes_head=True,
                            head_width=40, head_length=80, color='g', linewidth=2)
        displ_R = ax0.arrow(x_i, y_i, x[num] - x_i, y[num] - y_i, length_includes_head=True,
                            head_width=40, head_length=80, color='m', linewidth=2)
        displ_x = ax0.arrow(x_i, y_i, x[num] - x_i, 0, length_includes_head=True,
                            head_width=40, head_length=80, color='r', linewidth=2)
        displ_y = ax0.arrow(x[num], y_i, 0, y[num] - y_i, length_includes_head=True,
                            head_width=40, head_length=80, color='b', linewidth=2)

        return pos_x, pos_y, pos_R_1, pos_R_2, displ_R, displ_x, displ_y, \
            arr_1, arr_2, \
            plane_trajectory, plane_1, plane_2, plane_3, plane_4,
    else:
        arr_1 = ax1.arrow(t[num], a[num], 0, x[num] - a[num], length_includes_head=True,
                          head_width=0.1, head_length=40, color='r', linewidth=4)
        arr_2 = ax2.arrow(t[num], b[num], 0, y[num] - b[num], length_includes_head=True,
                          head_width=0.1, head_length=40, color='b', linewidth=4)
        displ_R = ax0.arrow(a[num], b[num], x[num] - a[num], y[num] - b[num], length_includes_head=True,
                            head_width=10, head_length=20, color='m', linewidth=2)
        displ_x = ax0.arrow(a[num], b[num], x[num] - a[num], 0, length_includes_head=True,
                            head_width=40, head_length=80, color='r', linewidth=2)
        displ_y = ax0.arrow(x[num], b[num], 0, y[num] - b[num], length_includes_head=True,
                            head_width=40, head_length=80, color='b', linewidth=2)

        # return pos_x,
        return pos_x, pos_y, displ_R, displ_x, displ_y, arr_1, arr_2, \
            plane_trajectory, plane_1, plane_2, plane_3, plane_4,


fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)

ax0 = fig.add_subplot(gs[0, :], facecolor=(0.9, 0.9, 0.9))

plane_1, = ax0.plot([], [], 'k', linewidth=10)
plane_2, = ax0.plot([], [], 'w', linewidth=5)
plane_3, = ax0.plot([], [], 'k', linewidth=4)
plane_4, = ax0.plot([], [], 'w', linewidth=3)

plane_trajectory, = ax0.plot([], [], '--k', linewidth=2)

if type == 3:
    plt.xlim(0, 2500)
    plt.ylim(150, 850)
else:
    plt.xlim(0, max(x))
    plt.ylim(0, max(y)+100)

plt.xlabel('position_x [m]', fontsize=15)
plt.ylabel('position_y [m]', fontsize=15)
plt.grid(True)

ax1 = fig.add_subplot(gs[1, 0], facecolor=(0.9, 0.9, 0.9))

if type == 1:
    pos_x, = ax1.plot([], [], '-b', linewidth=3, label='X = ' +
                      str(x_i)+' + ' + str(a) + 't')
elif type == 2:
    pos_x, = ax1.plot([], [], '-b', linewidth=3, label='X = ' +
                      str(x_i)+' + ' + str(a) + 't^2')
else:
    pos_x, = ax1.plot([], [], '-b', linewidth=3,
                      label='X = ' + str(0)+'*cos(2π' + str(f) + 't)')

if type == 3:
    plt.xlim(t0, t_end)
    plt.ylim(500, 1500)
else:
    plt.xlim(t0, t_end)
    plt.ylim(0, max(x))
plt.xlabel('time [s]', fontsize=15)
plt.ylabel('position_x [m]', fontsize=15)
plt.grid(True)
plt.legend(loc='lower right', fontsize='x-large')

ax2 = fig.add_subplot(gs[1, 1], facecolor=(0.9, 0.9, 0.9))

if type == 1:
    pos_y, = ax2.plot([], [], '-b', linewidth=3, label='Y = ' +
                      str(y_i) + ' + ('+str(b)+')t')
elif type == 2:
    pos_y, = ax2.plot([], [], '-b', linewidth=3, label='Y = ' +
                      str(y_i) + ' + ' + str(A)+' * sin(2π'+str(f)+'t)')
else:
    pos_y, = ax2.plot([], [], '-b', linewidth=3,
                      label='Y = ' + str(0)+'*sin(2π' + str(f) + 't)')

if type == 3:
    plt.xlim(t0, t_end)
    plt.ylim(0, 1000)
else:
    plt.xlim(t0, t_end)
    plt.ylim(0, max(y) + 100)
plt.xlabel('time [s]', fontsize=15)
plt.ylabel('position_y [m]', fontsize=15)
plt.grid(True)
plt.legend(loc='lower right', fontsize='x-large')


anim = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
