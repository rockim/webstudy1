import sys
import numpy as np
number = 0
array = []
count = 0
acount = 0
ar1 = []
ar2 = []
def make_Array():
    arr1 = np.identity(number)
    arr2 = np.identity(number)
    binary_arr1 = []
    binary_arr2 = []
    for j in range(number):
        binary_arr1 = convert_binary(int(ar1[j]))
        arr1[j] = binary_arr1[j]
        binary_arr2 = convert_binary(int(ar2[j]))
        arr2[j] = binary_arr2[j]
    print(arr1)
    print(arr2)
  #  for i in range(int(number[acount])):
        
def convert_array():
    global ar1, ar2
    count=0
    print(array)
    for i in array:
        #print(i.split(", ")[0].split("[")[1])
        if i == array[0]:
            ar1.insert(count,i.split(", ")[0].split("[")[1])
            count += 1
            for j in range(number-1):
            #print(i.split(", ")[j])
                if j != 0:
                    ar1.insert(count,i.split(", ")[j])
                    count += 1
            ar1.insert(count,i.split(", ")[number-1].split("]")[0])
            count += 1
        else:
            ar2.insert(count,i.split(", ")[0].split("[")[1])
            count += 1
            for j in range(number-1):
            #print(i.split(", ")[j])
                if j != 0:
                    ar2.insert(count,i.split(", ")[j])
                    count += 1
            ar2.insert(count,i.split(", ")[number-1].split("]")[0])
            count += 1

        #print(i.split(", ")[number-1].split("]")[0])
    print(ar1, ar2)
def convert_binary(int_num):
    binary_array = []
    if int_num < 2**(number-1):
        a = int_num
        while(a < 2**(number-1)):
            binary_array.append(0)
            a = a*2
    while(int_num != 0):
        if int_num%2==1:
            binary_array.append(1)
            int_num = int(int_num/2)
        else:
            binary_array.append(0)
            int_num = int(int_num/2)
    print(binary_array)
    return binary_array
#def convert_binary():

def opentxt():
    global number, array
    count = 0

    filepath = sys.path[0] + "/1.txt" #window일떄 "\\1.txt" linux 나 os X 일떄 "/1.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number= int(line.split("\n")[0]) #number < ["5","6"]
        elif len(line)>2:
            array.insert(count,line.split("\n")[0]) #array < ["[9,20,...]","[...]",...]
            count += 1
    convert_array()
def main():
    opentxt()
    make_Array()
    #for num in range(len(number)):
     #   number[num]

        
if __name__ == "__main__":
    main()
