import numpy as np


class Airplane:
    def __init__(self, t, a, n, altitude):
        self.frame_amount = len(t)

        self.a = a
        self.n = n
        self.t = t
        self.x = a*t**n  # x function

        self.altitude = altitude

        self.y = np.ones(len(t)) * self.altitude

        # Dot array
        self.dot = np.zeros(self.frame_amount)
        num_of_elements_per_chunk = 20
        for i in range(0, self.frame_amount):
            if i == num_of_elements_per_chunk:
                self.dot[i] = self.x[i]
                num_of_elements_per_chunk += 20
            else:
                self.dot[i] = self.x[num_of_elements_per_chunk-20]

        # Checking for 0
        if n < 1:
            t[0] = t[1]

        # Speed in the x direction (dx/dt)
        self.speed_x = n*a*t**(n-1)

    def __str__(self):
        return f"x function: {round(self.a, 1)} * t^{round(self.n, 1)}"

    def init_plot(self, sub_plot):
        self.plane_trajectory, = sub_plot.plot([], [], 'r:o', linewidth=2)
        self.plane_1, = sub_plot.plot([], [], 'k', linewidth=10)
        self.plane_2, = sub_plot.plot([], [], 'k', linewidth=5)
        self.plane_3, = sub_plot.plot([], [], 'k', linewidth=5)
        self.plane_4, = sub_plot.plot([], [], 'k', linewidth=3)
        self.plane_5, = sub_plot.plot([], [], 'k', linewidth=3)

    def init_second_plot(self, sub_plot, col):
        self.x_dist, = sub_plot.plot(
            [], [], col, linewidth=3, label='X = ' + str(int(self.a)) + '*t^' + str(round(self.n, 1)))

    def init_third_plot(self, sub_plot, col):
        self.speed, = sub_plot.plot([], [], col, linewidth=3, label='dX/dt = ' + str(
            self.n) + '*' + str(self.a) + '*t^(' + str(self.n-1) + ')')

    def update_plot(self, num):
        self.plane_trajectory.set_data(self.dot[0:num], self.y[0:num])
        self.plane_1.set_data([self.x[num] - 40, self.x[num] + 20],
                              [self.y[num], self.y[num]])
        self.plane_2.set_data([self.x[num] - 20, self.x[num]],
                              [self.y[num] + 0.3, self.y[num]])
        self.plane_3.set_data([self.x[num] - 20, self.x[num]],
                              [self.y[num] - 0.3, self.y[num]])
        self.plane_4.set_data([self.x[num] - 40, self.x[num] - 30],
                              [self.y[num] + 0.15, self.y[num]])
        self.plane_5.set_data([self.x[num] - 40, self.x[num] - 30],
                              [self.y[num] - 0.15, self.y[num]])

        self.x_dist.set_data(self.t[0:num], self.x[0:num])
        self.speed.set_data(self.t[0:num], self.speed_x[0:num])

        return self.plane_trajectory, self.plane_1, self.plane_2, self.plane_3, \
            self.plane_4, self.plane_5, self.x_dist, self.speed
