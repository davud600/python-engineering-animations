import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 60
dt = 0.04
t = np.arange(t0, t_end+dt, dt)

# water tank 1
volume_Tank1 = np.zeros(len(t))
for i in range(0, len(t)):
    if t[i] <= 22.5:
        volume_Tank1[i] = 50 + 2 * t[i]
    elif t[i] <= 32.5:
        volume_Tank1[i] = 95
    elif t[i] <= 32.5 + np.sqrt(45):
        volume_Tank1[i] = 95 - (t[i]-32.5)**2
    elif t[i] <= 42.5 + np.sqrt(45):
        volume_Tank1[i] = 50 + 1 * np.sin(2*np.pi*1*(t[i]-(32.5+np.sqrt(45))))
    else:
        volume_Tank1[i] = 50

# water tank 2
volume_Tank2 = np.zeros(len(t))
for i in range(0, len(t)):
    if t[i] <= 27.5:
        volume_Tank2[i] = 40 + 2 * t[i]
    elif t[i] <= 32.5:
        volume_Tank2[i] = 95
    elif t[i] <= 32.5 + np.sqrt(45):
        volume_Tank2[i] = 95 - (t[i]-32.5)**2
    elif t[i] <= 37.5 + np.sqrt(45):
        volume_Tank2[i] = 50 + 3 * np.sin(2*np.pi*1*(t[i]-(32.5+np.sqrt(45))))
    elif t[i] <= 42.5 + np.sqrt(45):
        volume_Tank2[i] = 50 + 1 * np.sin(2*np.pi*2*(t[i]-(37.5+np.sqrt(45))))
    else:
        volume_Tank2[i] = 50

# water tank 3
volume_Tank3 = np.zeros(len(t))
for i in range(0, len(t)):
    if t[i] <= 32.5:
        volume_Tank3[i] = 30 + 2 * t[i]
    elif t[i] <= 32.5 + np.sqrt(45):
        volume_Tank3[i] = 95 - (t[i]-32.5)**2
    elif t[i] <= 42.5 + np.sqrt(45):
        volume_Tank3[i] = 50 + (-1) * np.sin(2*np.pi *
                                             1*(t[i]-(32.5+np.sqrt(45))))
    else:
        volume_Tank3[i] = 50

############### Animation ###############
frame_amount = len(t)

radius = 5
volume_i = 0
volume_f = 100
dVol = 10


def update_plot(num):
    tank_1.set_data([-radius, radius], [volume_Tank1[num], volume_Tank1[num]])
    tank_12.set_height(volume_Tank1[num])

    tank_2.set_data([-radius, radius], [volume_Tank2[num], volume_Tank2[num]])
    tank_22.set_height(volume_Tank2[num])

    tank_3.set_data([-radius, radius], [volume_Tank3[num], volume_Tank3[num]])
    tank_32.set_height(volume_Tank3[num])

    tnk_1.set_data(t[0:num], volume_Tank1[0:num])
    tnk_1Z.set_data(t[0:num], volume_Tank1[0:num])

    tnk_2.set_data(t[0:num], volume_Tank2[0:num])
    tnk_2Z.set_data(t[0:num], volume_Tank2[0:num])

    tnk_3.set_data(t[0:num], volume_Tank3[0:num])
    tnk_3Z.set_data(t[0:num], volume_Tank3[0:num])

    return tank_12, tank_22, tank_32, tank_1, tank_2, tank_3, tnk_1, tnk_2, tnk_3, tnk_1Z, tnk_2Z, tnk_3Z


fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(2, 3)

ax0 = fig.add_subplot(gs[0, 0], facecolor=(0.9, 0.9, 0.9))
tank_1, = ax0.plot([], [], 'r', linewidth=4)
tank_12 = plt.Rectangle([-5, 0], 10, 0, facecolor='royalblue')
ax0.add_patch(tank_12)
plt.xlim(-radius, radius)
plt.ylim(0, volume_f)
plt.xticks(np.arange(-radius, radius + 1, 5))
plt.yticks(np.arange(0, volume_f+dVol, dVol))
plt.ylabel('tank volume [m^3]')
plt.title('Tank 1')

ax1 = fig.add_subplot(gs[0, 1], facecolor=(0.9, 0.9, 0.9))
tank_2, = ax1.plot([], [], 'r', linewidth=4)
tank_22 = plt.Rectangle([-5, 0], 10, 0, facecolor='royalblue')
ax1.add_patch(tank_22)
plt.xlim(-radius, radius)
plt.ylim(0, volume_f)
plt.xticks(np.arange(-radius, radius + 1, 5))
plt.yticks(np.arange(0, volume_f+dVol, dVol))
plt.title('Tank 2')

ax2 = fig.add_subplot(gs[0, 2], facecolor=(0.9, 0.9, 0.9))
tank_3, = ax2.plot([], [], 'r', linewidth=4)
tank_32 = plt.Rectangle([-5, 0], 10, 0, facecolor='royalblue')
ax2.add_patch(tank_32)
plt.xlim(-radius, radius)
plt.ylim(0, volume_f)
plt.xticks(np.arange(-radius, radius + 1, 5))
plt.yticks(np.arange(0, volume_f+dVol, dVol))
plt.title('Tank 3')

ax3 = fig.add_subplot(gs[1, 0:2], facecolor=(0.9, 0.9, 0.9))
tnk_1, = ax3.plot([], [], 'b', linewidth=3, label='Tank 1')
tnk_2, = ax3.plot([], [], 'g', linewidth=3, label='Tank 2')
tnk_3, = ax3.plot([], [], 'r', linewidth=3, label='Tank 3')
plt.xlim(0, t_end)
plt.ylim(0, volume_f)
plt.yticks(np.arange(0, volume_f+dVol, dVol))
plt.xticks([0, 22.5, 27.5, 32.5, 32.5+45**0.5, 37.5+45**0.5, 42.5+45**0.5, 60])
plt.xlabel('time [s]')
plt.ylabel('tank volume [m^3]')
plt.grid(True)
plt.legend(loc='upper right', fontsize='small')

ax4 = fig.add_subplot(gs[1, 2], facecolor=(0.9, 0.9, 0.9))
tnk_1Z, = ax4.plot([], [], 'b', linewidth=3)
tnk_2Z, = ax4.plot([], [], 'g', linewidth=3)
tnk_3Z, = ax4.plot([], [], 'r', linewidth=3)
# plt.xlim(32.5+45**0.5 - 1, 42.5+45**0.5 + 1)
# plt.ylim(50-3, 50+3)
plt.axis([38, 50, 47, 53])
plt.yticks([50])
plt.xticks([32.5+45**0.5, 37.5+45**0.5, 42.5+45**0.5])
plt.grid(True)

ani = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
