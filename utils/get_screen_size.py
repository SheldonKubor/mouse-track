"""
此模块仅用于获取屏幕设备大小

在App中 size=(self.winfo_screenwidth(), self.winfo_screenheight())
这样的方法获取到的屏幕尺寸大小有问题。win11，机械革命电脑，分辨率超过1080p，屏幕缩放倍数150%
"""
from PIL import ImageGrab
from functools import lru_cache

from service.types import Size
from screeninfo import get_monitors
from screeninfo.common import Monitor
import typing


@lru_cache(1)
def get_main_screen_size() -> Size:
    """
    获取主屏幕的大小
    """
    # return ImageGrab.grab().size
    return get_mutil_screen_size()


# 以后如果涉及多屏幕显示器
# 获取其中任意一个等方法
# 还可以继续在这里添加函数

def get_mutil_screen_size() -> Size:
    total_width = 0
    total_height = 0
    monitors = get_monitors()
    # for index, monitor in enumerate(monitors):
    #     screen_width = monitor.width
    #     screen_height = monitor.height

    #     total_width += screen_width
    #     max_height = max(max_height, screen_height)
    (start_x, start_y, end_x, end_y) = calculate_bounding_box(monitors)
    total_width = end_x - start_x
    total_height = end_y - start_y

    return total_width, total_height


# 计算多块屏幕拼接后的上下左右边界坐标，可以根据每块屏幕的坐标和大小进行计算。
# written by GPT-4o
def calculate_bounding_box(monitors: typing.List[Monitor]):
    # 初始化边界坐标
    start_x = float('inf')
    start_y = float('inf')
    end_x = float('-inf')
    end_y = float('-inf')

    for index, monitor in enumerate(monitors):
        start_x = min(start_x, monitor.x)
        start_y = min(start_y, monitor.y)
        end_x = max(end_x, monitor.x + monitor.width)
        end_y = max(end_y, monitor.y + monitor.height)

    return start_x, start_y, end_x, end_y
