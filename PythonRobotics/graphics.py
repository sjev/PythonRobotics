#!/usr/bin/env python
"""

Graphics for simulations, based on turtle graphics

Author  - Jev Kuznetsov

"""
from math import degrees
import turtle


class World:
    """ wrapper class for visualisations """

    def __init__(self, coord=(-10, -10, 10, 10)):
        """ create world with worldcoordinates as coord """

        self.screen = turtle.Screen()
        self.screen.setworldcoordinates(*coord)
        self.screen.tracer(0, 0)

        self.turtle = turtle.Turtle()
        self.turtle.color('blue')


    def robot_step(self, state):
        """ plot robot state """

        self.turtle.setpos(state.x, state.y)
        self.turtle.setheading(degrees(state.phi))
        self.screen.update()

    def plot_path(self, points, color='red',dotsize=10):
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
    print('Please close graphics window...')
    turtle.done()



if __name__ == "__main__":
    main()