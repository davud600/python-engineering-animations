import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration for animation
t0 = 0
t_end = 22
dt = 0.02
t = np.arange(0, t_end + dt, dt)

# rotating walls
rotating_wall_1_delay = 1  # [seconds]
rotating_wall_1_1_r = 20  # [meters]
rotating_wall_1_1_f = 1/10  # [hz]
rotating_wall_1_1_alpha_i = np.pi * 3/2  # [radians]

rotating_wall_1_1_alpha = []
for time_interval in t:
    max_alpha = 2 * np.pi  # [radians]
    alpha = 2 * np.pi * rotating_wall_1_1_f * \
        time_interval + rotating_wall_1_1_alpha_i
    if alpha >= max_alpha:
        alpha = max_alpha
    rotating_wall_1_1_alpha.append(alpha)

rotating_wall_1_1_x_i = 40  # [meters]
rotating_wall_1_1_y_i = 20  # [meters]
rotating_wall_1_1_x = rotating_wall_1_1_x_i + \
    rotating_wall_1_1_r * np.cos(rotating_wall_1_1_alpha)
rotating_wall_1_1_y = rotating_wall_1_1_y_i + \
    rotating_wall_1_1_r * np.sin(rotating_wall_1_1_alpha)
#
rotating_wall_1_2_r = 20  # [meters]
rotating_wall_1_2_f = 1/10  # [hz]
rotating_wall_1_2_alpha_i = np.pi * 1/2  # [radians]

rotating_wall_1_2_alpha = []
for time_interval in t:
    max_alpha = np.pi  # [radians]
    alpha = 2 * np.pi * rotating_wall_1_2_f * \
        time_interval + rotating_wall_1_2_alpha_i
    if alpha >= max_alpha:
        alpha = max_alpha
    rotating_wall_1_2_alpha.append(alpha)

rotating_wall_1_2_x_i = 40  # [meters]
rotating_wall_1_2_y_i = 20  # [meters]
rotating_wall_1_2_x = rotating_wall_1_2_x_i + \
    rotating_wall_1_2_r * np.cos(rotating_wall_1_2_alpha)
rotating_wall_1_2_y = rotating_wall_1_2_y_i + \
    rotating_wall_1_2_r * np.sin(rotating_wall_1_2_alpha)


rotating_wall_2_delay = 1  # [seconds]
rotating_wall_2_1_r = 20  # [meters]
rotating_wall_2_1_f = 1/10  # [hz]
rotating_wall_2_1_alpha_i = np.pi * 3/2  # [radians]

rotating_wall_2_1_alpha = []
for time_interval in t:
    max_alpha = 2 * np.pi  # [radians]
    alpha = 2 * np.pi * rotating_wall_2_1_f * \
        time_interval + rotating_wall_2_1_alpha_i
    if alpha >= max_alpha:
        alpha = max_alpha
    rotating_wall_2_1_alpha.append(alpha)

rotating_wall_2_1_x_i = 80  # [meters]
rotating_wall_2_1_y_i = 20  # [meters]
rotating_wall_2_1_x = rotating_wall_2_1_x_i + \
    rotating_wall_2_1_r * np.cos(rotating_wall_2_1_alpha)
rotating_wall_2_1_y = rotating_wall_2_1_y_i + \
    rotating_wall_2_1_r * np.sin(rotating_wall_2_1_alpha)
#
rotating_wall_2_2_r = 20  # [meters]
rotating_wall_2_2_f = 1/10  # [hz]
rotating_wall_2_2_alpha_i = np.pi * 1/2  # [radians]

rotating_wall_2_2_alpha = []
for time_interval in t:
    max_alpha = np.pi  # [radians]
    alpha = 2 * np.pi * rotating_wall_2_2_f * \
        time_interval + rotating_wall_2_2_alpha_i
    if alpha >= max_alpha:
        alpha = max_alpha
    rotating_wall_2_2_alpha.append(alpha)

rotating_wall_2_2_x_i = 80  # [meters]
rotating_wall_2_2_y_i = 20  # [meters]
rotating_wall_2_2_x = rotating_wall_2_2_x_i + \
    rotating_wall_2_2_r * np.cos(rotating_wall_2_2_alpha)
rotating_wall_2_2_y = rotating_wall_2_2_y_i + \
    rotating_wall_2_2_r * np.sin(rotating_wall_2_2_alpha)


# sliding walls
sliding_wall_1_delay = 3  # [seconds]
sliding_wall_1_1_x = 105  # [meters]
sliding_wall_1_1_v = 25  # [m/s]
sliding_wall_1_1_y_i = 20  # [meters]
sliding_wall_1_1_y = sliding_wall_1_1_y_i - \
    sliding_wall_1_1_v * t
#
sliding_wall_1_2_v = 25  # [m/s]
sliding_wall_1_2_y_i = 20  # [meters]
sliding_wall_1_2_y = sliding_wall_1_2_y_i + \
    sliding_wall_1_2_v * t

sliding_wall_2_delay = 3.5  # [seconds]
sliding_wall_2_1_x = 110  # [meters]
sliding_wall_2_1_v = 25  # [m/s]
sliding_wall_2_1_y_i = 20  # [meters]
sliding_wall_2_1_y = sliding_wall_2_1_y_i - \
    sliding_wall_2_1_v * t
#
sliding_wall_2_2_v = 25  # [m/s]
sliding_wall_2_2_y_i = 20  # [meters]
sliding_wall_2_2_y = sliding_wall_2_2_y_i + \
    sliding_wall_2_2_v * t

sliding_wall_3_delay = 4  # [seconds]
sliding_wall_3_1_x = 115  # [meters]
sliding_wall_3_1_v = 25  # [m/s]
sliding_wall_3_1_y_i = 20  # [meters]
sliding_wall_3_1_y = sliding_wall_3_1_y_i - \
    sliding_wall_3_1_v * t
#
sliding_wall_3_2_v = 25  # [m/s]
sliding_wall_3_2_y_i = 20  # [meters]
sliding_wall_3_2_y = sliding_wall_3_2_y_i + \
    sliding_wall_3_2_v * t

# plane 1 guide lines
plane_1_guide_lines_delay = 4.5  # [seconds]
plane_1_guide_line_1_y_i = 35  # [meters]
plane_1_guide_line_2_y_i = 25  # [meters]
plane_1_guide_line_v = 40  # [m/s]
plane_1_guide_line_x = plane_1_guide_line_v * (t - plane_1_guide_lines_delay)

# plane 2 guide lines
plane_2_guide_lines_delay = 4.5  # [seconds]
plane_2_guide_line_1_y_i = 5  # [meters]
plane_2_guide_line_2_y_i = 15  # [meters]
plane_2_guide_line_v = 40  # [m/s]
plane_2_guide_line_x = plane_2_guide_line_v * (t - plane_2_guide_lines_delay)

# plane 1
plane_1_delay = 6  # [seconds]
plane_1_a = 2  # [m/s^2]
plane_1_altitude = 30  # [meters]
plane_1_x_i = 5  # [meters]
plane_1_y = np.ones(len(t)) * plane_1_altitude
plane_1_x = plane_1_a * t**2 + plane_1_x_i

# plane 2
plane_2_delay = 6  # [seconds]
plane_2_a = 2  # [m/s^2]
plane_2_altitude = 10  # [meters]
plane_2_x_i = 5  # [meters]
plane_2_y = np.ones(len(t)) * plane_2_altitude
plane_2_x = plane_2_a * t**2 + plane_2_x_i

############### Animation ###############
frame_amount = len(t)


def update_plot(num):
    # rotating walls
    if t[num] >= rotating_wall_1_delay:
        time_interval_index = num - int(rotating_wall_1_delay / dt)
        rotating_wall_1_1.set_data([rotating_wall_1_1_x_i, rotating_wall_1_1_x[time_interval_index]], [
            rotating_wall_1_1_y_i, rotating_wall_1_1_y[time_interval_index]])
        rotating_wall_1_2.set_data([rotating_wall_1_2_x_i, rotating_wall_1_2_x[time_interval_index]], [
            rotating_wall_1_2_y_i, rotating_wall_1_2_y[time_interval_index]])
    if t[num] >= rotating_wall_2_delay:
        time_interval_index = num - int(rotating_wall_2_delay / dt)
        rotating_wall_2_1.set_data([rotating_wall_2_1_x_i, rotating_wall_2_1_x[time_interval_index]], [
            rotating_wall_2_1_y_i, rotating_wall_2_1_y[time_interval_index]])
        rotating_wall_2_2.set_data([rotating_wall_2_2_x_i, rotating_wall_2_2_x[time_interval_index]], [
            rotating_wall_2_2_y_i, rotating_wall_2_2_y[time_interval_index]])

    # sliding walls
    if t[num] >= sliding_wall_1_delay:
        time_interval_index = num - int(sliding_wall_1_delay / dt)
        sliding_wall_1_1.set_data(
            [sliding_wall_1_1_x, sliding_wall_1_1_x], [0, sliding_wall_1_1_y[time_interval_index]])
        sliding_wall_1_2.set_data(
            [sliding_wall_1_1_x, sliding_wall_1_1_x], [40, sliding_wall_1_2_y[time_interval_index]])
    if t[num] >= sliding_wall_2_delay:
        time_interval_index = num - int(sliding_wall_2_delay / dt)
        sliding_wall_2_1.set_data(
            [sliding_wall_2_1_x, sliding_wall_2_1_x], [0, sliding_wall_2_1_y[time_interval_index]])
        sliding_wall_2_2.set_data(
            [sliding_wall_2_1_x, sliding_wall_2_1_x], [40, sliding_wall_2_2_y[time_interval_index]])
    if t[num] >= sliding_wall_3_delay:
        time_interval_index = num - int(sliding_wall_3_delay / dt)
        sliding_wall_3_1.set_data(
            [sliding_wall_3_1_x, sliding_wall_3_1_x], [0, sliding_wall_3_1_y[time_interval_index]])
        sliding_wall_3_2.set_data(
            [sliding_wall_3_1_x, sliding_wall_3_1_x], [40, sliding_wall_3_2_y[time_interval_index]])

    # plane 1 guide lines
    if t[num] >= plane_1_guide_lines_delay:
        plane_1_guide_line_1.set_data(
            plane_1_guide_line_x[int(plane_1_guide_lines_delay/dt):num], plane_1_guide_line_1_y_i)
        plane_1_guide_line_2.set_data(
            plane_1_guide_line_x[int(plane_1_guide_lines_delay/dt):num], plane_1_guide_line_2_y_i)
    if t[num] >= plane_2_guide_lines_delay:
        plane_2_guide_line_1.set_data(
            plane_2_guide_line_x[int(plane_2_guide_lines_delay/dt):num], plane_2_guide_line_1_y_i)
        plane_2_guide_line_2.set_data(
            plane_2_guide_line_x[int(plane_2_guide_lines_delay/dt):num], plane_2_guide_line_2_y_i)

    # plane 1
    if t[num] >= plane_1_delay:
        time_interval_index = num - int(plane_1_delay / dt)
        plane_1_1.set_data(
            [plane_1_x[time_interval_index] - 5, plane_1_x[time_interval_index] + 2.5], [plane_1_y[time_interval_index], plane_1_y[time_interval_index]])
        plane_1_2.set_data(
            [plane_1_x[time_interval_index] - 2.5, plane_1_x[time_interval_index]], [plane_1_y[time_interval_index] + 3, plane_1_y[time_interval_index]])
        plane_1_3.set_data(
            [plane_1_x[time_interval_index] - 2.5, plane_1_x[time_interval_index]], [plane_1_y[time_interval_index] - 3, plane_1_y[time_interval_index]])
        plane_1_4.set_data(
            [plane_1_x[time_interval_index] - 5, plane_1_x[time_interval_index] - 3.75], [plane_1_y[time_interval_index] + 1.5, plane_1_y[time_interval_index]])
        plane_1_5.set_data(
            [plane_1_x[time_interval_index] - 5, plane_1_x[time_interval_index] - 3.75], [plane_1_y[time_interval_index] - 1.5, plane_1_y[time_interval_index]])

    # plane 2
    if t[num] >= plane_2_delay:
        time_interval_index = num - int(plane_2_delay / dt)
        plane_2_1.set_data(
            [plane_2_x[time_interval_index] - 5, plane_2_x[time_interval_index] + 2.5], [plane_2_y[time_interval_index], plane_2_y[time_interval_index]])
        plane_2_2.set_data(
            [plane_2_x[time_interval_index] - 2.5, plane_2_x[time_interval_index]], [plane_2_y[time_interval_index] + 3, plane_2_y[time_interval_index]])
        plane_2_3.set_data(
            [plane_2_x[time_interval_index] - 2.5, plane_2_x[time_interval_index]], [plane_2_y[time_interval_index] - 3, plane_2_y[time_interval_index]])
        plane_2_4.set_data(
            [plane_2_x[time_interval_index] - 5, plane_2_x[time_interval_index] - 3.75], [plane_2_y[time_interval_index] + 1.5, plane_2_y[time_interval_index]])
        plane_2_5.set_data(
            [plane_2_x[time_interval_index] - 5, plane_2_x[time_interval_index] - 3.75], [plane_2_y[time_interval_index] - 1.5, plane_2_y[time_interval_index]])

    return rotating_wall_1_1, rotating_wall_1_2, rotating_wall_2_1, rotating_wall_2_2, \
        sliding_wall_1_1, sliding_wall_1_2, sliding_wall_2_1, sliding_wall_2_2, sliding_wall_3_1, sliding_wall_3_2, \
        plane_1_guide_line_1, plane_1_guide_line_2, plane_2_guide_line_1, plane_2_guide_line_2, \
        plane_1_1, plane_1_2, plane_1_3, plane_1_4, plane_1_5, plane_2_1, plane_2_2, plane_2_3, plane_2_4, plane_2_5 \



fig = plt.figure(figsize=(16, 9), dpi=80, facecolor=(0.8, 0.8, 0.8))
gs = gridspec.GridSpec(1, 2)
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.85,
                    top=0.75, wspace=0.15, hspace=0.2)


ax0 = fig.add_subplot(gs[:, 0:2], facecolor=(0.9, 0.9, 0.9))

x_lim = 120
y_lim = 40

plt.xlim(0, x_lim)
plt.ylim(0, y_lim)
plt.xticks(np.arange(0, x_lim + 1, 10))
plt.yticks([])
plt.grid(True)

# static walls
static_wall_1, = ax0.plot(
    [0, x_lim], [y_lim / 2, y_lim / 2], 'lightgray', linewidth=10)

# rotating walls
rotating_wall_1_1, = ax0.plot(
    [rotating_wall_1_1_x_i, rotating_wall_1_1_x_i], [0, y_lim / 2], 'gray', linewidth=15)
rotating_wall_1_2, = ax0.plot(
    [rotating_wall_1_2_x_i, rotating_wall_1_2_x_i], [y_lim / 2, y_lim], 'gray', linewidth=15)
rotating_wall_2_1, = ax0.plot(
    [rotating_wall_2_1_x_i, rotating_wall_2_1_x_i], [0, y_lim / 2], 'gray', linewidth=15)
rotating_wall_2_2, = ax0.plot(
    [rotating_wall_2_2_x_i, rotating_wall_2_2_x_i], [y_lim / 2, y_lim], 'gray', linewidth=15)

# sliding walls
sliding_wall_1_1, = ax0.plot([sliding_wall_1_1_x, sliding_wall_1_1_x], [
                             0, y_lim / 2], 'gray', linewidth=25)
sliding_wall_1_2, = ax0.plot(
    [sliding_wall_1_1_x, sliding_wall_1_1_x], [y_lim / 2, y_lim], 'gray', linewidth=25)
sliding_wall_2_1, = ax0.plot([sliding_wall_2_1_x, sliding_wall_2_1_x], [
                             0, y_lim / 2], 'gray', linewidth=25)
sliding_wall_2_2, = ax0.plot(
    [sliding_wall_2_1_x, sliding_wall_2_1_x], [y_lim / 2, y_lim], 'gray', linewidth=25)
sliding_wall_3_1, = ax0.plot([sliding_wall_3_1_x, sliding_wall_3_1_x], [
                             0, y_lim / 2], 'gray', linewidth=25)
sliding_wall_3_2, = ax0.plot(
    [sliding_wall_3_1_x, sliding_wall_3_1_x], [y_lim / 2, y_lim], 'gray', linewidth=25)

# plane 1 guide lines
plane_1_guide_line_1, = ax0.plot([], [], '--b', linewidth=2)
plane_1_guide_line_2, = ax0.plot([], [], '--b', linewidth=2)

# plane 2 guide lines
plane_2_guide_line_1, = ax0.plot([], [], '--g', linewidth=2)
plane_2_guide_line_2, = ax0.plot([], [], '--g', linewidth=2)

# plane 1
plane_1_1, = ax0.plot([plane_1_x_i - 5, plane_1_x_i + 2.5],
                      [plane_1_altitude, plane_1_altitude], 'b', linewidth=7)
plane_1_2, = ax0.plot([plane_1_x_i - 2.5, plane_1_x_i],
                      [plane_1_altitude + 3, plane_1_altitude], 'b', linewidth=8)
plane_1_3, = ax0.plot([plane_1_x_i - 2.5,
                      plane_1_x_i], [plane_1_altitude - 3, plane_1_altitude], 'b', linewidth=8)
plane_1_4, = ax0.plot([plane_1_x_i - 5,
                      plane_1_x_i - 3.75], [plane_1_altitude + 1.5, plane_1_altitude], 'b', linewidth=2.5)
plane_1_5, = ax0.plot([plane_1_x_i - 5, plane_1_x_i - 3.75],
                      [plane_1_altitude - 1.5, plane_1_altitude], 'b', linewidth=2.5)


# plane 2
plane_2_1, = ax0.plot([plane_2_x_i - 5, plane_2_x_i + 2.5],
                      [plane_2_altitude, plane_2_altitude], 'g', linewidth=7)
plane_2_2, = ax0.plot([plane_2_x_i - 2.5, plane_2_x_i],
                      [plane_2_altitude + 3, plane_2_altitude], 'g', linewidth=8)
plane_2_3, = ax0.plot([plane_2_x_i - 2.5,
                      plane_2_x_i], [plane_2_altitude - 3, plane_2_altitude], 'g', linewidth=8)
plane_2_4, = ax0.plot([plane_2_x_i - 5,
                      plane_2_x_i - 3.75], [plane_2_altitude + 1.5, plane_2_altitude], 'g', linewidth=2.5)
plane_2_5, = ax0.plot([plane_2_x_i - 5, plane_2_x_i - 3.75],
                      [plane_2_altitude - 1.5, plane_2_altitude], 'g', linewidth=2.5)


ani = animation.FuncAnimation(
    fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)
plt.show()
