from turtle import width
from urllib.parse import SplitResult
from pkg_resources import split_sections
import pyecharts.options as opts
from pyecharts.charts import Line
import datetime

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=line-simple

目前无法实现的功能:

暂无
"""
f = open("D:\\standjump_press.txt")
text = f.readlines()
x_data = [1, 2]
y_data = [1, 2]
i = 0
while i < len(text):
    x_data.append(i)
    y_data.append(int(text[i]))
    i = i+1


# print(x_data)
print(y_data)

time =datetime.datetime.now()
timestr =  datetime.datetime.strftime(time,'%H-%M-%S')


(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="value"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),

        ),

    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )

    .render(timestr+"standjump_press.html")
)
