#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2018/9/22


import unittest
'''
基于测试⽅方法级别的setUp, tearDown

执行每个测试方法的时候都会执行一次setUp 和tearDown
'''


class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print ("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_1st')
        self.assertEqual(self.foo.pop(), 9)

    def test_2nd(self):
        print('test_2nd')
        print("test_2nd:"+str(self.foo))
        self.assertEqual(self.foo.pop(), 8)

    @classmethod
    def tearDownClass(self):
        print("end method")


if __name__ == '__main__':
    unittest.main()

