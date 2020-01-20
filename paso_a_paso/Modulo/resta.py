def resta(*args):
    result = 0
    for i in args:
        l = len(args)
        if result == 0:
            print("if")
            result = i
            if args[l-1] == result and args[l-1] == i:
                print("elif")
                result = -i
        else:
            print("else")
            result -= i
    return result
