# encoding: utf-8
# @Time : 20/08/07 23:10
# @Author : Xu Bai
# @File : ivtk观察管线.py
# @Desc :

from tvtk.api import tvtk
from pyface.api import GUI
from tvtk.tools import ivtk

s = tvtk.CubeSource(x_length=1.0,y_length=2.0,z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)

# 创建一个带有Crust（Python shell）的窗口
gui = GUI()
win = ivtk.IVTKWithCrustAndBrowser()
win.open()
win.scene.add_actor(a)

# 开启界面消息循环
gui.start_event_loop()