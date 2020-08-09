# encoding: utf-8
# @Time : 20/08/09 16:53
# @Author : Xu Bai
# @File : tvtk数据加载.py
# @Desc :
from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop

'''
STL文件是在计算图像应用系统中用来表示三角形网格的文件格式
Plot3D文件是广泛用于NASA，规则格网的数据文件。分为网格文件（XYZ）、空气动力学结果文件（Q文件）、通用结果文件
'''
s = tvtk.STLReader(file_name="python.stl")
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)



win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()

print("PLOT3D START:\n")
def read_data():
    plot3d = tvtk.MultiBlockPLOT3DReader(
        xyz_file_name="combxyz.bin",
        q_file_name="combq.bin",
        scalar_function_number=100,  # 设置标量数据数量
        vector_function_number=200  # 矢量数据数量
    )
    plot3d.update()
    return plot3d

plot3d = read_data()
grid = plot3d.output.get_block(0)
print(grid.points.to_array())