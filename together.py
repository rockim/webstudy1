import sys
import numpy as np
number = 0
array = []
def make_Array():
    arr1 = np.identity(number)
    arr2 = np.identity(number)

    for i in range(number):
        for j in range(number):
            arr1[i][j]
  #  for i in range(int(number[acount])):
        
def convert_array():
    ar1 = []
    ar2 = []
    count=0
    print(array)
    for i in array:
        if i == array[0]:
            ar1.insert(count,i.split(", ")[0].split("[")[1])
            count += 1
            for j in range(number-1):
                if j != 0:
                    ar1.insert(count,i.split(", ")[j])
                    count += 1
            ar1.insert(count,i.split(", ")[number-1].split("]")[0])
            count += 1
        else:
            ar2.insert(count,i.split(", ")[0].split("[")[1])
            count += 1
            for j in range(number-1):
                if j != 0:
                    ar2.insert(count,i.split(", ")[j])
                    count += 1
            ar2.insert(count,i.split(", ")[number-1].split("]")[0])
            count += 1
    print(ar1, ar2) # array 에 받은 것을 ar1 과 ar2 로 나누어서 저장
#def convert_binary():

def opentxt():
    global number, array
    count = 0
    filepath = sys.path[0] + "\\1.txt" #window일떄 "\\1.txt" linux 나 os X 일떄 "/1.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number= int(line.split("\n")[0]) #number = 5
        elif len(line)>2:
            array.insert(count,line.split("\n")[0]) #array < ["[9,20,...]","[...]",...]
            count += 1
    #print(array[0].split(", ")[0].split("[")[1])
    #print(array[0].split(", ")[number-1].split("]")[0])
    convert_array()
def main():
    opentxt()
    #for num in range(len(number)):
     #   number[num]

        
if __name__ == "__main__":
    main()
