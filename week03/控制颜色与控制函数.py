# encoding: utf-8
# @Time : 20/08/13 14:06
# @Author : Xu Bai
# @File : 控制颜色与控制函数.py
# @Desc :
'''
colormap定义的颜色，也叫Look Up Table
'''
import numpy as np
from mayavi import mlab

x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)

mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')
mlab.show()

print('更改物体的透明度信息')
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)

mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')
# 访问surf对象的LUT
lut = surf.module_manager.scalar_lut_manager.lut.table.to_array()
# 增加透明梯度，修改alpha通道
lut[:, -1] = np.linspace(0, 255, 256)
surf.module_manager.scalar_lut_manager.lut.table = lut
mlab.show()
