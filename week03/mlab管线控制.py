# encoding: utf-8
# @Time : 20/08/14 22:45
# @Author : Xu Bai
# @File : mlab管线控制.py
# @Desc :
import numpy as np
from mayavi import mlab
from mayavi.tools import pipeline
x, y, z = np.ogrid[-10:10:20j,-10:10:20j,-10:10:20j]
s = np.sin(x * y * z) / (x * y * z)
print('生成标量数据')
mlab.contour3d(s)
mlab.show()
print('切平面')
