# encoding: utf-8
# @Time : 20/08/06 23:30
# @Author : Xu Bai
# @File : tvtk安装测试.py
# @Desc :
from tvtk.tools import tvtk_doc
from tvtk.api import tvtk

tvtk_doc.main()
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
print(s)