# lab03.py
# Eldor Bekpulatov (eb654)
# Sep 7, 2016

def first_inside_quotes(s):
    
    beg=s.index('"')
    mid=s[beg+1:]
    end=mid.index('"')
    res=mid[:end]
    
    return res