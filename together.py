import sys
import re

number = []
array = []
dex = []
final =[]
answer = []


def opentxt():
    global number, array
    count = 0
    filepath = sys.path[0] + "\\0.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number = int(line)
        elif len(line)>2:
            array.insert(count,line.split("\n")[0])
            count +=1;

    arr1 = re.findall("\d+",array[0])
    arr2 = re.findall("\d+",array[1])

    for i in range(number):
        dex.append(int(arr1[i])|int(arr2[i]))  

    for i in dex:
        str(final.append(bin(i)[2:]))


    for i in range(number):
        final[i] = final[i].replace('0',' ')
        final[i] = final[i].replace('1','#')

    print(final)




def main():
    opentxt()

if __name__ == "__main__":
    main()
