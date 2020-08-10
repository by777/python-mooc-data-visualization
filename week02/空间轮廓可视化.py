# encoding: utf-8
# @Time : 20/08/10 14:08
# @Author : Xu Bai
# @File : 空间轮廓可视化.py
# @Desc :
'''
tvtk.StructuredGridOutlineFilter()
计算PolyData对象的外边框
'''
from tvtkfunc import ivtk_scene,event_loop
from tvtk.api import tvtk
from tvtk.common import configure_input

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name = "combxyz.bin",
    q_file_name = "combq.bin",
    scalar_function_number = 100,
    vector_function_number = 200
)
plot3d.update()
grid = plot3d.output.get_block(0)
# 计算表示外边框的PolyData对象
outline = tvtk.StructuredGridOutlineFilter()
configure_input(outline,grid)

m = tvtk.PolyDataMapper(input_connection=outline.output_port)
a = tvtk.Actor(mapper=m)

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()