# encoding: utf-8
# @Time : 20/08/10 13:37
# @Author : Xu Bai
# @File : 标量数据可视化.py
# @Desc :
'''
等值面过滤器
tvtk.ContourFilter()
:方法
generate_values(): 设置n条等值线的值，一般用于重新绘制等值线
set_value(): 设定一条等值线的值，一般用于覆盖某条等值线或者新增加一条等值线
'''
from tvtkfunc import ivtk_scene,event_loop
from tvtk.api import tvtk

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name = "combxyz.bin",
    q_file_name = "combq.bin",
    scalar_function_number = 100,
    vector_function_number = 200
)
plot3d.update()
grid = plot3d.output.get_block(0)

# 创建一个等值面对象
con = tvtk.ContourFilter()
# 将网格与其绑定
con.set_input_data(grid)
# 创建10个等值面
con.generate_values(10,grid.point_data.scalars.range)

m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=con.output_port)
a = tvtk.Actor(mapper=m)
a.property.opacity = 0.5

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()