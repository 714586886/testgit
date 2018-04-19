# -*- coding: utf-8 -*-

def yield_test(n):
    for i in range(n):
        yield call(i)

    print('do something.')
    print('end.')

def call(i):
    return i*2

for j in yield_test(5):
    print(j)