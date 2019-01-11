# 4:02  4:08

def all_true(iterable):
    for item in iterable:
    	if item != 1:
    		return False
    return True

def any_true(iterable):
    for item in iterable:
    	if item == 1:
    		return True
    return False

def main():
    a = all_true( [1, 0, 1, 1, 1] )
    b = all_true( [1, 1, 1, 1, 1] )
    c = any_true( [0, 0, 0, 1, 1] )
    d = any_true( [0, 0 ,0 ,0, 0] )

    print(a, b, c, d) #Should be: False True True False

main()