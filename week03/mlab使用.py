# encoding: utf-8
# @Time : 20/08/12 14:36
# @Author : Xu Bai
# @File : mlab使用.py
# @Desc :
'''
mlab是mayavi提供的面向脚本的api，可以实现快速的三维可视化

步骤：
1. 建立数据源
2. 使用Filter对数据加工（可选）
3. 添加可视化模块

Point3d：基于Numpy数组x,y,z提供的三维点坐标，绘制点图形

Plot3d： 基于1维Numpy数组x,y,z提供的三维坐标数据，绘制线图形
    tube_radius: 线管的半径
    tube_sides: 默认6，表示线的分段数
'''

import numpy as np
from mayavi import mlab

print("------------scale_factor------------\n")
# linespace：以等差数列建立数组
t = np.linspace(0, 4 * np.pi, 20)
x = np.sin(2 * t)
y = np.cos(t)
z = np.cos(2 * t)
s = 2 + np.sin(t)
# 对数据可视化 scale_factor: 放缩比例
points = mlab.points3d(x, y, z, s, colormap="Reds", scale_factor=.25)
mlab.show()

print("------------plot3d------------\n")
# 建立数据
n_mer, n_long = 6, 11
dphi = np.pi / 1000.0
phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
mu = phi * n_mer
x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
z = np.sin(n_long * mu / n_mer) * 0.5
l = mlab.plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap="Spectral")
mlab.show()

print("------------imshow()------------\n")
s = np.random.random((10, 10))
img = mlab.imshow(s, colormap='gist_earth')
mlab.show()

print("------------surf()------------\n")


def f(x, y):
    return np.sin(x - y) + np.cos(x + y)


x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
s = mlab.surf(x, y, f)
mlab.show()

print("------------contour_surf()------------\n")
s = mlab.contour_surf(x, y, f)
mlab.show()

print("------------contour3d()------------\n")
x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
scalars = x * x + y * y + z * z
obj = mlab.contour3d(scalars, contours=8, transparent=True)
mlab.show()

print("------------quiver3d()------------\n")
x, y, z = np.mgrid[-1:3, -2:3, -2:3]
r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y * np.sin(r) / (r + 0.001)
v = -x * np.sin(r) / (r + 0.001)
w = np.zeros_like(z)
obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
mlab.show()
