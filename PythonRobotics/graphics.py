#!/usr/bin/env python
"""

Graphics for simulations, based on turtle graphics

Author  - Jev Kuznetsov

"""
import math
from time import sleep
import turtle

TESTING = True


class World:
    """ wrapper class for visualisations """

    def __init__(self, coord=(-10, -10, 10, 10), window_size=(800, 800)):
        """ create world with worldcoordinates as coord """

        self.screen = turtle.Screen()
        self.screen.setup(width=window_size[0], height=window_size[1])
        self.screen.setworldcoordinates(*coord)
        self.screen.tracer(0, 0)
        self.screen.onclick(self.click_callback)

        self.turtle = turtle.Turtle()
        self.turtle.color('blue')

        self._markers = {}  # marker objects
        self.click_xy = None  # last clicked position

    def click_callback(self, x, y):
        self.click_xy = (x, y)

    def add_marker(self,
                   name,
                   color='green',
                   shape="circle",
                   size=0.5,
                   trace=False):
        """ add marker (markers are Turtle objects) """
        m = turtle.Turtle()
        m.color(color)
        m.shape(shape)
        m.shapesize(size, size)
        if not trace:
            m.penup()
        self._markers[name] = m

    def move_marker(self, name, xy):
        """move marker to a position

        Args:
            name (str): marker name
            xy (Vector): (x,y) vector
        """

        self._markers[name].setpos(xy)
        self.screen.update()

    def move_robot(self, xy, phi):
        """ plot robot state """

        self.turtle.setpos(xy)
        self.turtle.setheading(math.degrees(phi))
        self.screen.update()

    def plot_path(self, points, color='red', dotsize=3):
        """ plot conntected points """

        t = turtle.Turtle()
        t.color(color)

        t.hideturtle()
        for x, y in points:
            t.setpos(x, y)
            t.dot(dotsize)
        self.screen.update()


def main():
    """ demo function """

    w = World()

    # plot path
    points = [(-5, -5), (0, 0), (0, 2),
              (2, 2), (2, 0), (2, -2), (5, 5)]

    w.plot_path(points)

    w.add_marker('m')
    for x in range(10):
        w.move_marker('m', (x/10, 0))
        w.move_robot((0, x), math.pi/2)
        if not TESTING:
            sleep(0.1)

    if not TESTING:
        print('Please close graphics window...')
        turtle.done()


if __name__ == "__main__":
    main()
