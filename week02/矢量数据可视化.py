# encoding: utf-8
# @Time : 20/08/10 13:54
# @Author : Xu Bai
# @File : 矢量数据可视化.py
# @Desc :
'''
tvtk.Glyph3D()符号化技术
为了方便表现，常对数据降维
tvtk.MaskPoints()对数据降采样
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
# 对数据集中的数据进行随机选取，每50个点选择一个点
mask = tvtk.MaskPoints(random_mode=True,on_ratio=50)
mask.set_input_data(grid)
# 创建表示箭头的PolyData数据集
glyph_source = tvtk.ArrowSource()
# 在mask采样后的数据集PolyData上每个点放置一个箭头
# 箭头的方向、长度和颜色由于点对应的矢量和标量数据决定
# scale_factor数据共同放缩系数
glyph = tvtk.Glyph3D(input_connection=mask.output_port,
                     scale_factor=4)
glyph.set_source_connection(glyph_source.output_port)
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=glyph.output_port)
a = tvtk.Actor(mapper=m)

win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
