# coding=utf-8

import os
import Utils, Rename

root_dir = "/Volumes/XiaoMi-usb0/下载"

tool = Rename.RenameTool()


def get_suffix(file_name):
    index = file_name.rfind('.')
    return file_name[index:len(file_name)]


def folder_rename(root_dir):
    file_list = os.listdir(root_dir)
    for file_name in filter(Utils.hasChinese, file_list):
        print("老文件名:", file_name)
        tool.find_fitness_movie(file_name)
        new_file_name = tool.new_filename + get_suffix(file_name)
        print("新文件名:", new_file_name)
        os.rename(root_dir + "/" + file_name, root_dir + "/" + new_file_name)


def single_rename(path, file_name):
    print("老文件名:", file_name)
    tool.find_fitness_movie(file_name)
    new_file_name = tool.new_filename + get_suffix(file_name)
    print("新文件名:", new_file_name)
    os.rename(path + "/" + file_name, path + "/" + new_file_name)


single_rename("/Volumes/XiaoMi-usb0/下载", "火星救援.The Martian.2015.评分[8.4].主演[马特·达蒙].导演[雷德利·斯科特].Mp4Ba")
# folder_rename(root_dir)
