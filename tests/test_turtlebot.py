#!/usr/bin/env python
"""
Test turtlebot simulator

author - Jev Kuznetsov
"""

import conftest
from PythonRobotics import turtlebot as m


def test_1():
    m.PLOT_RESULT = False
    m.main()


if __name__ == '__main__':
    conftest.run_this_test(__file__)
