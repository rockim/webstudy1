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
<<<<<<< HEAD
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



=======
    filepath = sys.path[0] + "\\1.txt" #window일떄 "\\1.txt" linux 나 os X 일떄 "/1.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number.append(line.split("\n")[0]) #number < ["5","6"]
        elif len(line)>2:
            array.insert(count,line.split("\n")[0]) #array < ["[9,20,...]","[...]",...]
            count += 1
>>>>>>> de4b6bca1ffe884e2c63cab8a8c6f9eed407a33f

def main():
    opentxt()

if __name__ == "__main__":
    main()
