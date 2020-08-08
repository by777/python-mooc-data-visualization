# encoding: utf-8
# @Time : 20/08/08 14:37
# @Author : Xu Bai
# @File : 数据集.py
# @Desc :
'''

数据集（Dataset）
1. 点（Point）和数据（Data）
2. 点之间：连接、非连接
3. 单元（Cell）：多个相关的点组成单元
4. 点的连接：显式、隐式
5. 数据：标量（Scalar）、矢量（Vector）
---------------------------------------
数据集的分类：
ImageData: 表示二维或三维图像的数据结构
RectilinearGrid: 间距不均匀的网格，所有点都在正交的网格上
StructuredGrid: 创建任意形状的网格，需要指定点的坐标
PolyData: 由一系列的点、点之间的练习以及由点构成的多边形组成
UnstructuredGrid: 
'''

from tvtk.api import tvtk
import numpy as np

print("\n----------------------ImageData----------------------")
img = tvtk.ImageData(
    # origin: 三维网格数据的起点坐标
    # spacing: 三维数据再X、Y、Z上点的间距
    # dimensions：X、Y、Z上的网格数
    spacing=(1,1,1),origin=(1,2,3),dimensions=(3,4,5))

print(img.get_point(0))

print("前6个点坐标\n")
for n in range(6):
    print("%.1f, %.1f, %.1f" % img.get_point(n))

print("\n----------------------RectilinearGrid----------------------")
x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x),len(y),len(z)
print("前6个点坐标\n")
for n in range(6):
    print(r.get_point(n))