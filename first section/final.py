import numpy as np

import animation
import airplane

anim = animation.Animation(t_end=2, dt=0.005, t0=0)
anim.init_figure()

# Airplanes
plane_1 = airplane.Airplane(t=anim.t, a=800, n=1, altitude=2.5)
plane_2 = airplane.Airplane(t=anim.t, a=400, n=2, altitude=1.5)
plane_3 = airplane.Airplane(t=anim.t, a=200, n=3, altitude=0.5)

# Subplot 1
anim.add_subplot(row_index=0, col_slice=slice(None))

plane_1.init_plot(sub_plot=anim.get_sub_plots(0))
plane_2.init_plot(sub_plot=anim.get_sub_plots(0))
plane_3.init_plot(sub_plot=anim.get_sub_plots(0))

anim.set_xlim(plane_1.x[0], plane_1.x[-1])
anim.set_ylim(0, plane_1.y[-1])
anim.set_xticks(np.arange(0, plane_1.x[-1] + 1, plane_1.x[-1]/4))
anim.set_yticks(np.arange(
    0, plane_1.y[-1] + 1, plane_1.y[-1]/plane_1.y[-1]))
anim.set_xlabel('x-distance')
anim.set_ylabel('y-distance')
anim.set_grid(True)

# Subplot 2
anim.add_subplot(row_index=1, col_slice=0)

plane_1.init_second_plot(sub_plot=anim.get_sub_plots(1), col='-r')
plane_2.init_second_plot(sub_plot=anim.get_sub_plots(1), col='-b')
plane_3.init_second_plot(sub_plot=anim.get_sub_plots(1), col='-g')

anim.set_xlim(anim.t[0], anim.t[-1])
anim.set_ylim(plane_1.x[0], plane_1.x[-1])
anim.set_xticks(np.arange(anim.t[0], anim.t[-1] + anim.dt, anim.t[-1] / 4))
anim.set_yticks(np.arange(plane_1.x[0], plane_1.x[-1] + 1, plane_1.x[-1] / 4))
anim.set_xlabel('time [hrs]')
anim.set_ylabel('x-distance [km]')
anim.set_title('x-distance VS time')
anim.set_legend(loc='upper left')
anim.set_grid(True)

# Subplot 3
anim.add_subplot(row_index=1, col_slice=1)

plane_1.init_third_plot(sub_plot=anim.get_sub_plots(2), col='-r')
plane_2.init_third_plot(sub_plot=anim.get_sub_plots(2), col='-b')
plane_3.init_third_plot(sub_plot=anim.get_sub_plots(2), col='-g')

anim.set_xlim(anim.t[0], anim.t[-1])
anim.set_ylim(0, plane_1.speed_x[-1] * 2)
anim.set_xticks(np.arange(anim.t[0], anim.t[-1] + anim.dt, anim.t[-1] / 4))
anim.set_yticks(np.arange(
    plane_1.speed_x[0], plane_1.speed_x[-1] * 2 + 1, plane_1.speed_x[-1] * 2 / 4))
anim.set_xlabel('time [hrs]')
anim.set_ylabel('speed [km/hr]')
anim.set_title('x-distance VS time')
anim.set_grid(True)
anim.set_legend(loc='upper right')


def update_plot(num):
    return plane_3.update_plot(num)


anim.show_animation(update_plot=update_plot)
