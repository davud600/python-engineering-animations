import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(0, t_end+dt, dt)

g_Earth = -9.8
g_Mars = -3.7
g_Moon = -1.6

n = 2
y_i = 100

# Y Pos
y_Earth = y_i+0.5*g_Earth*t**n
y_Mars = y_i+0.5*g_Mars*t**n
y_Moon = y_i+0.5*g_Moon*t**n

# Velocity - dy / dt
y_Earth_velocity = n*0.5*g_Earth*t**(n-1)
y_Mars_velocity = n*0.5*g_Mars*t**(n-1)
y_Moon_velocity = n*0.5*g_Moon*t**(n-1)

# Acceleration - d^2y / dt^2
y_Earth_Acceleration = (n-1)*g_Earth*t**(n-2)
y_Mars_Acceleration = (n-1)*g_Mars*t**(n-2)
y_Moon_Acceleration = (n-1)*g_Moon*t**(n-2)


def create_circle(r):
    degrees = np.arange(0, 361, 1)
    radians = degrees*np.pi/180
    sphere_x = r*np.cos(radians)
    sphere_y = r*np.sin(radians)
    return sphere_x, sphere_y


# Earth circle
radius_Earth = 5
sphere_x_Earth, sphere_y_Earth = create_circle(radius_Earth)

# Mars circle
radius_Mars = 10
sphere_x_Mars, sphere_y_Mars = create_circle(radius_Mars)

# Moon circle
radius_Moon = 20
sphere_x_Moon, sphere_y_Moon = create_circle(radius_Moon)


############### Animation ###############

frame_amount = len(t)
width_ratio = 1.2
y_f = -10
dy = 10


def update_plot(num):
    if y_Earth[num] >= radius_Earth:
        sphere_Earth.set_data(sphere_x_Earth, sphere_y_Earth+y_Earth[num])
        alt_Earth.set_data(t[0:num], y_Earth[0:num])
        vel_Earth.set_data(t[0:num], y_Earth_velocity[0:num])
        acc_Earth.set_data(t[0:num], y_Earth_Acceleration[0:num])
    if y_Mars[num] >= radius_Mars:
        sphere_Mars.set_data(sphere_x_Mars, sphere_y_Mars+y_Mars[num])
        alt_Mars.set_data(t[0:num], y_Mars[0:num])
        vel_Mars.set_data(t[0:num], y_Mars_velocity[0:num])
        acc_Mars.set_data(t[0:num], y_Mars_Acceleration[0:num])
    if y_Moon[num] >= radius_Moon:
        sphere_Moon.set_data(sphere_x_Moon, sphere_y_Moon+y_Moon[num])
        alt_Moon.set_data(t[0:num], y_Moon[0:num])
        vel_Moon.set_data(t[0:num], y_Moon_velocity[0:num])
        acc_Moon.set_data(t[0:num], y_Moon_Acceleration[0:num])

    return sphere_Earth, alt_Earth, vel_Earth, acc_Earth, \
        sphere_Mars, alt_Mars, vel_Mars, acc_Mars, \
        sphere_Moon, alt_Moon, vel_Moon, acc_Moon, \



fig = plt.figure(figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(3, 4)

# Earth subplot
ax0 = fig.add_subplot(gs[:, 0], facecolor=(0.9, 0.9, 0.9))
sphere_Earth, = ax0.plot([], [], 'k', linewidth=3)
land_Earth, = ax0.plot([-radius_Earth*width_ratio, radius_Earth *
                        width_ratio], [-5, -5], 'b', linewidth=38)

plt.xlim(-radius_Earth*width_ratio, radius_Earth*width_ratio)
plt.ylim(y_f+dy, y_i+dy)
plt.xticks(np.arange(-radius_Earth, radius_Earth+1, radius_Earth))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))

# Mars subplot
ax0 = fig.add_subplot(gs[:, 1], facecolor=(0.9, 0.9, 0.9))
sphere_Mars, = ax0.plot([], [], 'k', linewidth=3)
land_Mars, = ax0.plot([-radius_Mars*width_ratio, radius_Mars *
                       width_ratio], [-5, -5], 'orangered', linewidth=38)

plt.xlim(-radius_Mars*width_ratio, radius_Mars*width_ratio)
plt.ylim(y_f+dy, y_i+dy)
plt.xticks(np.arange(-radius_Mars, radius_Mars+1, radius_Mars))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))

# Moon subplot
ax0 = fig.add_subplot(gs[:, 2], facecolor=(0.9, 0.9, 0.9))
sphere_Moon, = ax0.plot([], [], 'k', linewidth=3)
land_Moon, = ax0.plot([-radius_Moon*width_ratio, radius_Moon *
                       width_ratio], [-5, -5], 'gray', linewidth=38)

plt.xlim(-radius_Moon*width_ratio, radius_Moon*width_ratio)
plt.ylim(y_f+dy, y_i+dy)
plt.xticks(np.arange(-radius_Moon, radius_Moon+1, radius_Moon))
plt.yticks(np.arange(y_f, y_i+2*dy, dy))

# Altitude subplot
ax3 = fig.add_subplot(gs[0, 3], facecolor=(0.9, 0.9, 0.9))
alt_Earth, = ax3.plot([], [], 'blue', linewidth=3, label='Alt_Earth = ' +
                      str(y_i)+' + (' + str(round(g_Earth/2, 1))+')t^'+str(n)+' [m]')
alt_Mars, = ax3.plot([], [], 'orangered', linewidth=3, label='Alt_Mars = ' +
                     str(y_i)+' + (' + str(round(g_Mars/2, 1))+')t^'+str(n)+' [m]')
alt_Moon, = ax3.plot([], [], 'gray', linewidth=3, label='Alt_Moon = ' +
                     str(y_i)+' + (' + str(round(g_Moon/2, 1))+')t^'+str(n)+' [m]')
plt.xlim(0, t_end)
plt.ylim(0, y_i)
plt.legend(loc=(0.6, 0.7), fontsize='x-small')

# Velocity subplot
ax4 = fig.add_subplot(gs[1, 3], facecolor=(0.9, 0.9, 0.9))
vel_Earth, = ax4.plot([], [], 'blue', linewidth=3, label='Vel_Earth = ' +
                      str(n) + str(round(g_Earth/2, 1)) + 't^'+str(n-1) + ' [m/s]')
vel_Mars, = ax4.plot([], [], 'orangered', linewidth=3, label='Vel_Mars = ' +
                     str(n) + str(round(g_Mars/2, 1)) + 't^'+str(n-1) + ' [m/s]')
vel_Moon, = ax4.plot([], [], 'gray', linewidth=3, label='Vel_Moon = ' +
                     str(n) + str(round(g_Moon/2, 1)) + 't^'+str(n-1) + ' [m/s]')
plt.xlim(0, t_end)
plt.ylim(-y_i, 0)
plt.legend(loc=(0.01, 0.01), fontsize='x-small')

# Acceleration subplot
ax5 = fig.add_subplot(gs[2, 3], facecolor=(0.9, 0.9, 0.9))
acc_Earth, = ax5.plot([], [], 'blue', linewidth=3, label='Acc_Earth = ' +
                      str(round(g_Earth, 2)) + '[(m/s)/s ≡ m/s]^2')
acc_Mars, = ax5.plot([], [], 'orangered', linewidth=3, label='Acc_Mars = ' +
                     str(round(g_Mars, 2)) + '[(m/s)/s ≡ m/s]^2')
acc_Moon, = ax5.plot([], [], 'gray', linewidth=3, label='Acc_Moon = ' +
                     str(round(g_Moon, 2)) + '[(m/s)/s ≡ m/s]^2')
plt.xlim(0, t_end)
plt.ylim(-11, 0)
plt.legend(loc=(0.01, 0.35), fontsize='x-small')

plane_anim = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
