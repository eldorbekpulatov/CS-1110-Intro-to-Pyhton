# test13.py
# Walker White (wmw2)
# November 10, 2016
"""Test cases for lab13.py"""

import cornelltest
import lab13


def test_minpos1():
    """Test the function minpos1"""
    print '  Testing minpos1'
    a = [0,3,4,2,5,1]
    cornelltest.assert_equals(0, lab13.minpos1(a,0,5))
    cornelltest.assert_equals(5, lab13.minpos1(a,1,5))
    cornelltest.assert_equals(3, lab13.minpos1(a,1,4))
    print '  minpos1 looks okay'


def test_minpos2():
    """Test the function minpos2"""
    print '  Testing minpos2'
    a = [0,3,4,2,5,1]
    cornelltest.assert_equals(0, lab13.minpos1(a,0,5))
    cornelltest.assert_equals(5, lab13.minpos1(a,1,5))
    cornelltest.assert_equals(3, lab13.minpos1(a,1,4))
    print '  minpos2 looks okay'


def test_fixedpart1():
    """Test the function fixedpartition1"""
    print '  Testing fixedpartition1'
    a = [0,7,3,6,8,2,1]
    pivot = lab13.fixedpartition1(a)
    cornelltest.assert_equals(4, pivot)
    cornelltest.assert_equals([0,1,3,6,2], a[:pivot+1])
    cornelltest.assert_equals([8,7], a[pivot+1:])
    a = [0,1,2,6,7,8,9]
    pivot = lab13.fixedpartition1(a)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([0,1,2,6], a[:pivot+1])
    cornelltest.assert_equals([8,9,7], a[pivot+1:])
    print '  fixedpartition1 looks okay'


def test_fixedpart2():
    """Test the function fixedpartition2"""
    print '  Testing fixedpartition2'
    a = [0,7,3,6,8,2,1]
    pivot = lab13.fixedpartition2(a)
    cornelltest.assert_equals(4, pivot)
    cornelltest.assert_equals([0,1,3,6,2], a[:pivot+1])
    cornelltest.assert_equals([8,7], a[pivot+1:])
    a = [0,1,2,6,7,8,9]
    pivot = lab13.fixedpartition2(a)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([0,1,2,6], a[:pivot+1])
    cornelltest.assert_equals([8,9,7], a[pivot+1:])
    print '  fixedpartition2 looks okay'


def test_partition2():
    """Test the function partition2"""
    print '  Testing partition2'
    a = [5,7,3,6,8,2,1]
    pivot = lab13.partition2(a,0,6)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([1,3,2,5], a[:pivot+1])
    cornelltest.assert_equals([8, 6, 7], a[pivot+1:])
    a = [5,7,3,6,8,2,1]
    pivot = lab13.partition2(a,2,5)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([5,7,2,3], a[:pivot+1])
    cornelltest.assert_equals([8,6,1],   a[pivot+1:])
    pivot = lab13.partition2(a,1,4)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([5,2,3,7], a[:pivot+1])
    cornelltest.assert_equals([8, 6, 1], a[pivot+1:])
    a = [6,1,2,5,7,8,9]
    pivot = lab13.partition2(a,0,6)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([1,2,5,6], a[:pivot+1])
    cornelltest.assert_equals([8,9,7], a[pivot+1:])
    print '  partition2 looks okay'


def test_partition3():
    """Test the function partition3"""
    print '  Testing partition3'
    a = [5,7,3,6,8,2,1]
    pivot = lab13.partition3(a,0,6)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([3,2,1,5], a[:pivot+1])
    cornelltest.assert_equals([8, 7, 6], a[pivot+1:])
    a = [5,7,3,6,8,2,1]
    pivot = lab13.partition3(a,2,5)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([5,7,2,3], a[:pivot+1])
    cornelltest.assert_equals([8,6,1],   a[pivot+1:])
    pivot = lab13.partition3(a,1,4)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([5,2,3,7], a[:pivot+1])
    cornelltest.assert_equals([8, 6, 1], a[pivot+1:])
    a = [6,1,2,5,7,8,9]
    pivot = lab13.partition3(a,0,6)
    cornelltest.assert_equals(3, pivot)
    cornelltest.assert_equals([1,2,5,6], a[:pivot+1])
    cornelltest.assert_equals([7,8,9],   a[pivot+1:])
    print '  partition3 looks okay'


def test_dnf2():
    """Test the function dnf2"""
    print '  Testing dnf2'
    a = [0,-1,1,0,1,-1]
    bands = lab13.dnf2(a)
    cornelltest.assert_equals(2, bands[0])
    cornelltest.assert_equals(4, bands[1])
    cornelltest.assert_equals([-1,-1], a[:bands[0]])
    cornelltest.assert_equals([ 0, 0], a[bands[0]:bands[1]])
    cornelltest.assert_equals([ 1, 1], a[bands[1]:])
    a = [0,4,3,2,1,0,-1,-2,-3,-4,0]
    bands = lab13.dnf2(a)
    cornelltest.assert_equals(4, bands[0])
    cornelltest.assert_equals(7, bands[1])
    cornelltest.assert_equals([-4,-3,-2,-1], a[:bands[0]])
    cornelltest.assert_equals([ 0, 0, 0],    a[bands[0]:bands[1]])
    cornelltest.assert_equals([ 1, 2, 3, 4], a[bands[1]:])
    print '  dnf2 looks okay'


def test_dnf3():
    """Test the function dnf3"""
    print '  Testing dnf3'
    a = [0,-1,1,0,1,-1]
    bands = lab13.dnf3(a)
    cornelltest.assert_equals(2, bands[0])
    cornelltest.assert_equals(4, bands[1])
    cornelltest.assert_equals([-1,-1], a[:bands[0]])
    cornelltest.assert_equals([ 0, 0], a[bands[0]:bands[1]])
    cornelltest.assert_equals([ 1, 1], a[bands[1]:])
    a = [0,4,3,2,1,0,-1,-2,-3,-4,0]
    bands = lab13.dnf3(a)
    cornelltest.assert_equals(4, bands[0])
    cornelltest.assert_equals(7, bands[1])
    cornelltest.assert_equals([-4,-3,-2,-1], a[:bands[0]])
    cornelltest.assert_equals([ 0, 0, 0],    a[bands[0]:bands[1]])
    cornelltest.assert_equals([ 1, 2, 3, 4], a[bands[1]:])
    print '  dnf3 looks okay'


def test_sort1():
    """Test the function sort1"""
    print '  Testing sort1'
    a = [0,3,2,6,4,8,7,5]
    lab13.sort1(a)
    cornelltest.assert_equals([0,2,3,4,5,6,7,8], a)
    lab13.sort1(a)
    cornelltest.assert_equals([0,2,3,4,5,6,7,8], a)
    a = [6,5,4,3,2,1,0]
    lab13.sort1(a)
    cornelltest.assert_equals([0,1,2,3,4,5,6], a)
    print '  sort1 looks okay'


def test_sort2():
    """Test the function sort2"""
    print '  Testing sort2'
    a = [0,3,2,6,4,8,7,5]
    lab13.sort1(a)
    cornelltest.assert_equals([0,2,3,4,5,6,7,8], a)
    lab13.sort1(a)
    cornelltest.assert_equals([0,2,3,4,5,6,7,8], a)
    a = [6,5,4,3,2,1,0]
    lab13.sort1(a)
    cornelltest.assert_equals([0,1,2,3,4,5,6], a)
    print '  sort2 looks okay'


# Script Code
if __name__ == '__main__':
    print 'Testing sequence algorithms'
    # COMMENT OUT THE FUNCTIONS YOU IMPLEMENT
    test_minpos1()
    test_minpos2()
    print ''
    test_fixedpart1()
    test_fixedpart2()
    print ''
    test_partition2()
    test_partition3()
    print ''
    test_dnf2()
    test_dnf3()
    print ''
    test_sort1()
    test_sort2()
    print "Module lab13.py is working correctly"