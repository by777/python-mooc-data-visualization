# encoding: utf-8
# @Time : 20/08/06 23:31
# @Author : Xu Bai
# @File : 创建三维对象.py
# @Desc :

'''
traits:(属性)
CubeSource：立方体三维数据对象数据源
ConeSource: 圆锥
CylinderSource： 圆柱
ArcSource：圆弧
ArrowSource： 箭头
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
