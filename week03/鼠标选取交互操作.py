# encoding: utf-8
# @Time : 20/08/13 14:16
# @Author : Xu Bai
# @File : 鼠标选取交互操作.py
# @Desc :
'''
选取红色小球问题分析：
1. 建立一个figure figure = mlab.gcf()
2. 随机生成红、白小球 mlab.points3d()
3. 初始化红色小球选取外框 def picker_callback(picker)
4. 鼠标选取任意红色小球，外框移动到该小球上（callback）
5. 建立on_mouse_pick()响应机制 picker = figure.on_mouse_pick(picker_callback)

'''