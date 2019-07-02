import sys
number = []
array = []

def opentxt():
    global number, array
    count = 0
    filepath = sys.path[0] + "\\1.txt"
    lines=open(filepath,'r').readlines()
    for line in lines:
        if len(line)==2:
            number.append(line.split("\n")[0])
        elif len(line)>2:
            array.insert(count,line.split("\n")[0])
            count += 1

def main():
    opentxt()

if __name__ == "__main__":
    main()
