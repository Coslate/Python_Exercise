#! /usr/bin/env python3.6

#Author  : Coslate
#Purpose : This program split the list by non-integer
#Date    : 2017/12/02


def IsNumber(s) :
    try :
        float(s)
        return True
    except:
        return False

def main() :
    dict_ans = {}
    sample_in = ["i", "j", 123, 999, "k", 462, 777, 97, "h", 444]
    key = ""
    count = 0

    for i in sample_in :
    #    print("i = {x}, (i == str) = {y}".format(x = i, y = IsNumber(i)))
        if(not IsNumber(i)) :
            count = 0
            key = i
        else :
            if(count == 0) :
                dict_ans[key] = [i]
            else :
                dict_ans[key].append(i)
            count += 1

    for i, j in dict_ans.items() :
        print("dict[{x}] = {y}".format(x = i, y = j))




#---------------Execution---------------#
if(__name__ == '__main__') :
    main()
