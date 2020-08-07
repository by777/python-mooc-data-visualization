# encoding: utf-8
# @Time : 20/08/06 23:31
# @Author : Xu Bai
# @File : 创建三维对象.py
# @Desc : 利用pipeline创建图形对象窗口

'''
traits:(属性)
CubeSource：立方体三维数据对象数据源
ConeSource: 圆锥
CylinderSource： 圆柱
ArcSource：圆弧
ArrowSource： 箭头

管线：
可视化管线（Visualization Pipeline）：将原始数据加工成图形数据的过程
图形管线（Graphics Pipeline）：将图形数据加工成我们看到的图像的过程

过程：
①数据 <-> ②数据预处理 <-> ③数据映射 <-> ④绘制（Rendering） <-> ⑤显示（Display）
其中①②是可视化管线
对应CubeSource（PolyData）和PolyDataMapper(Mapper)
③④⑤是图形管线：
Actor：场景中的一个实体，它包括一个图形数据（mapper），具有描述该实体的位置、方向、大小的属性
Renderer：渲染的场景。它包括多个要渲染的Actor
RenderWindow：渲染用的图形窗口，包含一个或多个Render
RenderWindowInteracor：提供交互功能
'''

from tvtk.api import tvtk

# resolution底面圆分辨率，36边形近似圆形
# s = tvtk.ConeSource(height=3.0, radius=1.0, resolution=36)
# print(s)

# 显示一个长方体

s = tvtk.CubeSource(x_length=1.0,y_length=2.0,z_length=3.0)

# 使用PolyDataMapper将数据转换为图像数据
m = tvtk.PolyDataMapper(input_connection=s.output_port)

# 创建一个Actor实体
a = tvtk.Actor(mapper=m)

# 创建一个渲染器Renderer，将Actor添加
r = tvtk.Renderer(background=(0,0,0))
r.add_actor(a)

# 创建一个绘制窗口RenderWindow，将Renderer添加进去
w = tvtk.RenderWindow(size=(300,300))
w.add_renderer(r)

# 创建一个RenderWindowInteractor窗口交换工具
i = tvtk.RenderWindowInteractor(render_window=w)

# 开启交互
i.initialize()
i.start()
