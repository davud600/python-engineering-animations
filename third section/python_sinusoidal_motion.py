import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 16
dt = 0.02
t = np.arange(0, t_end+dt, dt)

# Blue train
f1 = 0.125
A1 = 7
train_blue = A1*np.sin(2*np.pi*f1*t)

# Red train
f2 = 0.125
A2 = -7
train_red = A2*np.cos(2*np.pi*f2*t)

# Cars
y_i = 13
delay_green = 2
delay_purple = 6
car_green = y_i-2*(t-delay_green)**2
car_purple = y_i-2*(t-delay_purple)

############### Animation ###############
frame_amount = len(t)


def update_plot(num):
    X_blue.set_data(t[0:num], train_blue[0:num])
    X_red.set_data(t[0:num], train_red[0:num])

    block_blue.set_data(
        [train_blue[num]-0.45, train_blue[num]+0.45], [3.5, 3.5])
    block_red.set_data(
        [train_red[num]-0.45, train_red[num]+0.45], [1.5, 1.5])

    if t[num] >= delay_green:
        block_green.set_data(
            [3.5, 3.5], [car_green[num]-0.5, car_green[num]+0.5])
        Y_green.set_data(t[int(delay_green/dt):num],
                         car_green[int(delay_green/dt):num])
    else:
        block_green.set_data(
            [3.5, 3.5], [y_i-0.5, y_i+0.5])
        Y_green2.set_data(t[0:num], y_i)

    if t[num] >= delay_purple:
        block_purple.set_data(
            [-3.5, -3.5], [car_purple[num]-0.5, car_purple[num]+0.5])
        Y_purple.set_data(t[int(delay_purple/dt):num],
                          car_purple[int(delay_purple/dt):num])
    else:
        block_purple.set_data(
            [-3.5, -3.5], [y_i-0.5, y_i+0.5])
        Y_purple2.set_data(t[0:num], y_i)

    return X_blue, X_red, block_blue, block_red, block_purple, Y_purple, Y_purple2, \
        block_green, Y_green, Y_green2,


fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 2)

# Subplot 0
ax0 = fig.add_subplot(gs[0, 0], facecolor=(0.9, 0.9, 0.9))
X_blue, = ax0.plot([], [], '-b', linewidth=3,
                   label='X_blue = ' + str(A1) + '*sin(2n*'+str(f1)+'*t')
X_red, = ax0.plot([], [], '-r', linewidth=3,
                  label='X_red = ' + str(A2) + '*cos(2n*'+str(f2)+'*t')
plt.xlim(t0, t_end)
plt.ylim(-max(A1, A2)-1, max(A1, A2)+1)
plt.xlabel('time [s]')
plt.ylabel('X [m]')
plt.grid(True)
ax0.spines['bottom'].set_position('center')
ax0.xaxis.set_label_coords(0.5, 0)
plt.legend(bbox_to_anchor=(1.1, 1.2), fontsize='medium')

# Subplot 1
ax1 = fig.add_subplot(gs[1, 0], facecolor=(0.9, 0.9, 0.9))
Y_green, = ax1.plot([], [], 'g', linewidth=3)
Y_green2, = ax1.plot([], [], 'g', linewidth=3, alpha=1)
Y_purple, = ax1.plot([], [], 'm', linewidth=5)
Y_purple2, = ax1.plot([], [], 'm', linewidth=5, alpha=1)
plt.xlim(t0, t_end)
plt.ylim(-2, y_i+1)
plt.xlabel('time [s]')
plt.ylabel('Y [m]')
plt.grid(True)
ax1.spines['bottom'].set_position(['data', 0])
ax1.xaxis.set_label_coords(0.5, 0)

# Subplot 2
ax2 = fig.add_subplot(gs[:, 1], facecolor=(0.9, 0.9, 0.9))
block_blue, = ax2.plot([], [], '-b', linewidth=28)
block_red, = ax2.plot([], [], '-r', linewidth=28)
block_green, = ax2.plot([], [], '-g', linewidth=24)
block_purple, = ax2.plot([], [], 'purple', linewidth=24)

# Danger zones
danger_zone1_1, = ax2.plot([3, 4], [1, 1], '-k', linewidth=3)
danger_zone1_2, = ax2.plot([3, 4], [2, 2], '-k', linewidth=3)
danger_zone1_2, = ax2.plot([3, 3], [1, 2], '-k', linewidth=3)
danger_zone1_2, = ax2.plot([4, 4], [1, 2], '-k', linewidth=3)

danger_zone2_1, = ax2.plot([3, 4], [3, 3], '-k', linewidth=3)
danger_zone2_2, = ax2.plot([3, 4], [4, 4], '-k', linewidth=3)
danger_zone2_2, = ax2.plot([3, 3], [3, 4], '-k', linewidth=3)
danger_zone2_2, = ax2.plot([4, 4], [3, 4], '-k', linewidth=3)

danger_zone3_1, = ax2.plot([-3, -4], [1, 1], '-k', linewidth=3)
danger_zone3_2, = ax2.plot([-3, -4], [2, 2], '-k', linewidth=3)
danger_zone3_2, = ax2.plot([-3, -3], [1, 2], '-k', linewidth=3)
danger_zone3_2, = ax2.plot([-4, -4], [1, 2], '-k', linewidth=3)

danger_zone4_1, = ax2.plot([-3, -4], [3, 3], '-k', linewidth=3)
danger_zone4_2, = ax2.plot([-3, -4], [4, 4], '-k', linewidth=3)
danger_zone4_2, = ax2.plot([-3, -3], [3, 4], '-k', linewidth=3)
danger_zone4_2, = ax2.plot([-4, -4], [3, 4], '-k', linewidth=3)

bbox_green = dict(boxstyle='square', fc=(0.9, 0.9, 0.9), ec='g', lw=1)
bbox_purple = dict(boxstyle='square', fc=(0.9, 0.9, 0.9), ec='purple', lw=1)
ax2.text(0, y_i+1.5, 'car_green='+str(int(y_i)) +
         '-2(t-2)^2', size=10, color='g', bbox=bbox_green)
ax2.text(-max(A1, A2)-0.5, y_i+1.5, 'car_purple='+str(int(y_i)) +
         '-2(t-6)', size=10, color='purple', bbox=bbox_purple)

plt.xlim(-max(A1, A2)-2, max(A1, A2)+2)
plt.ylim(-2, y_i+1)
plt.grid(True)
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position(['data', 0])
plt.xticks(np.concatenate(
    [np.arange(-max(A1, A2)-1, 0, 1), np.arange(1, max(A1, A2)+2, 1)]))
plt.yticks(np.concatenate([np.arange(-2, 0, 1), np.arange(1, y_i+2, 1)]))

ani = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
