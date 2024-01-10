import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np


class Animation:
    def __init__(self, t_end, dt=0.005, t0=0):
        self.t0 = t0
        self.t_end = t_end
        self.dt = dt
        self.t = np.arange(self.t0, self.t_end+self.dt, self.dt)  # [hr]
        self.frame_amount = len(self.t)
        self.sub_plots = []

    def init_figure(self, figsize=(16, 9), dpi=120, facecolor=(0.8, 0.8, 0.8), grid_spec_x=2, grid_spec_y=2):
        self.fig = plt.figure(figsize=figsize, dpi=dpi,
                              facecolor=facecolor)
        self.gs = gridspec.GridSpec(grid_spec_x, grid_spec_y)

    def add_subplot(self, row_index, col_slice, facecolor=(0.9, 0.9, 0.9)):
        self.sub_plots.append(self.fig.add_subplot(
            self.gs[row_index, col_slice], facecolor=facecolor))

    def get_figure(self):
        return self.fig

    def get_gs(self):
        return self.gs

    def get_sub_plots(self, index):
        return self.sub_plots[index]

    def set_xlim(self, x0, xf):
        plt.xlim(x0, xf)

    def set_ylim(self, y0, yf):
        plt.ylim(y0, yf)

    def set_xticks(self, ticks, size=15):
        plt.xticks(ticks, size=size)

    def set_yticks(self, ticks, size=15):
        plt.yticks(ticks, size=size)

    def set_xlabel(self, label, fontsize=15):
        plt.xlabel(label, fontsize=fontsize)

    def set_ylabel(self, label, fontsize=15):
        plt.xlabel(label, fontsize=fontsize)

    def set_title(self, title, fontsize=20):
        plt.xlabel(title, fontsize=fontsize)

    def set_grid(self, set):
        plt.grid(set)

    def set_legend(self, loc, fontsize='x-large'):
        plt.legend(loc=loc, fontsize=fontsize)

    def show_animation(self, update_plot, interval=20, repeat=True, blit=True):
        self.animation = animation.FuncAnimation(
            self.fig, update_plot, frames=self.frame_amount, interval=interval, repeat=repeat, blit=blit)
        plt.show()
