#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Haul"
# Email: 790542969@qq.com
# Date: 2018/9/22

import unittest
import logging
'''
基于模块级别的 setUpModule，tearDownModule

执行此模块里的所有类里的测试⽅方法，只执行一次setup 和teardown


'''


def setUpModule():
    print("setup method\n")
    global foo
    foo = list(range(10))

class simple_test(unittest.TestCase):

    def test_1st(self):
        logging.info('info')
        logging.error('error')
        print('simple_test1_1'+str(foo))
        self.assertEqual(foo.pop(), 9)

    def test_2nd(self):
        print('simple_test1_2' + str(foo))
        self.assertEqual(foo.pop(), 8)

class simple_test2(unittest.TestCase):

    def test_1st(self):
        #foo=[0,....,,,7]
        print('simple_test2_1' + str(foo))
        self.assertEqual(foo.pop(), 7)

    def test_2nd(self):
        print('simple_test2_2' + str(foo))
        self.assertEqual(foo.pop(), 6)

def tearDownModule():
    print("end method")

if __name__ == '__main__':
    unittest.main()