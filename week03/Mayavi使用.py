# encoding: utf-8
# @Time : 20/08/11 14:26
# @Author : Xu Bai
# @File : Mayavi使用.py
# @Desc :
'''
mayavi:
功能：
1. 处理图像可视化和图像操作的mlab模块
2. 操作管线对象、窗口对象的api

mayavi的层级：
1. Engine: 建立和销毁Scenes
2. Scenes: 数据集合Sources
3. Filters: 对数据进行变换
4. Module Manager：控制颜色等
5. Modules: 最终数据的表示，线条平面等
'''
from mayavi import mlab
from numpy import pi, sin, cos, mgrid

x = [[-1, 1, 1, -1, -1], [-1, 1, 1, -1, -1]]
y = [[-1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
z = [[1, 1, -1, -1, 1], [1, 1, -1, -1, 1]]
s = mlab.mesh(x, y, z)
input("按下按键")
# 更复杂一点的例子
dphi, dtheta = pi / 250.0, pi / 250.0
[phi, theta] = mgrid[0:pi + dphi * 1.5: dphi, 0:2 * pi + dtheta * 1.5:dtheta]
m0 = 4
m1 = 3
m2 = 2
m3 = 3
m4 = 6
m5 = 2
m6 = 6
m7 = 4
r = sin(m0 * phi) ** m1 + cos(m2 ** phi) ** m3 + sin(m4 * theta) ** m5 + cos(m6 * theta) ** m7
x = r * sin(phi) * cos(theta)
y = r * cos(phi)
z = r * sin(phi) * sin(theta)

# 对该数据三维可视化
s = mlab.mesh(x, y, z)
mlab.show()
