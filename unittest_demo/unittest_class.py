#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2018/9/22

import unittest

'''
基于类级别的 setUpClass, tearDownClass

执行这个类里面的所有测试⽅方法只有一次执行setup, tearDown
'''

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("init \n")
        simple_test.foo = list(range(10))
        print(str(simple_test.foo))

    def test_1st(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 9)

    def test_2nd(self):
        print(str(simple_test.foo))
        self.assertEqual(simple_test.foo.pop(), 8)

    @classmethod
    def tearDownClass(cls):
        print("end class")

if __name__ == '__main__':
    unittest.main()