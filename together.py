import sys
import re
import pdb
number = []
array = []
path1 = []
path2 = []

def opentxt():
    global number, array
    count = 0
    filepath = sys.path[0] + "\\2.txt" #window일떄 "\\1.txt" linux 나 os X 일떄 "/1.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number.append(line.split("\n")[0]) #number < ["5","6"]
        elif len(line)>2:
            array.insert(count,line.split("\n")[0]) #array < ["[9,20,...]","[...]",...]
            count += 1

def calculate():
    global number, path1, path2
    tmp = []
    n = int(number[0])
    # save only numbers
    path1 = re.findall("\d+", array[0])
    path2 = re.findall("\d+", array[1])

    # caculate bitwise or
    for i in range(n):
        a = int(path1[i])
        b = int(path2[i])
        tmp.append(a|b)
    
    # change to binary code
    for i in range(n):
        tmp[i] = bin(tmp[i])

    # change to "#" and " "
    for i in range(n):
        tmp[i] = change(tmp[i])

    # print result
    print(tmp)

def change(num):
    tmp = ""
    n = int(number[0])

    # if binary code is short
    if (len(num) < 2+ n):
        for i in range(2+n - len(num)):
            tmp = tmp + " "
        for i in range(2, len(num)):
            if (num[i] == "0"):
                tmp = tmp + " "
            else:
                tmp = tmp + "#"

    # if binary code is not short
    else:
        for i in range(2, len(num)):
            if (num[i] == "0"):
                tmp = tmp +" "
            else:
                tmp = tmp +"#"
    return tmp

def main(): 
    opentxt()
    calculate()

if __name__ == "__main__":
    main()
