#!/bin/python3

__author__ = "Manoj Kumar Arram"

import numpy


n, m = input().split()

numpy.set_printoptions(sign=' ')
print(numpy.eye(int(n), int(m)))

