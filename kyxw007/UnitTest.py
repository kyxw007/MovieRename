# coding=utf-8
import unittest
import Rename
import time

file_name = "震荡效应.原盘中英字幕.Concussion.2015.BD1080P.X264.AAC.English.CHS-ENG.Mp4Ba"
kewords = ["震荡", "效应", "原", "盘中", "英", "字幕"]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        t1=time.time()
        tool = Rename.RenameTool()
        movie = tool.find_fitness_movie("震荡效应.原盘中英字幕.Concussion.2015.BD1080P.X264.AAC.English.CHS-ENG.Mp4Ba")
        print("最佳匹配电影:",movie['title'],"|",movie['original_title'])
        print("新文件名:",tool.get_new_filename())
        t2=time.time()
        print("耗时:",t2-t1)
        assert movie['title'],"震荡效应"


if __name__ == '__main__':
    unittest.main()
