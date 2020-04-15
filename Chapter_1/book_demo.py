# @Time     : 2020/1/17 13:33
# @Auther   : zsy
# @File     : book_demo.py
"""
二分法 猜数字
"""
from comment_func import func_time


@func_time
def binary_search(my_list: list, item: int) -> int:
    """
    二分法排序
    :param my_list: 查找列表
    :param item: 所需要查找的元素
    :return: 索引位置, 没有找到返回 -1
    """
    low_index = 0
    hight_index = len(my_list) - 1
    while low_index <= hight_index:
        mid = (low_index + hight_index) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight_index = mid - 1
        else:
            low_index = mid + 1

    return -1


if __name__ == '__main__':
    random_list = [1, 3, 5, 7, 9]
    print(binary_search(random_list, 3))
