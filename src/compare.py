import subprocess
import random
import sys
import os

def produceSafeFile(fileType):
    while True:
        randomName = str(random.randint(0,1000000000)) + '.' + fileType
        if not os.path.exists(randomName):
            break
    return randomName

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Invalid usage format')
        print('python3 compare.py code1 code2 inputGenerator numberOfTests timeOut')
        print('code1/code2 : python file location to compare result')
        print('inputGenerator : input generating script')
        print('numberOfTests : number of tests to run')
        print('timeOut : How many time to spend')
        exit(0)
    code1 = sys.argv[1]
    code2 = sys.argv[2]
    codeG = sys.argv[3]
    trial = int(sys.argv[4])
    tle = float(sys.argv[5])
    inputfile = produceSafeFile('i')
    output1 = produceSafeFile('o')
    output2 = produceSafeFile('o')
    for times in range(trial):
        try:
            subprocess.run(["python3 " + codeG +  " > " + inputfile], timeout=tle, shell=True)
            f = open(inputfile)
            inputString = f.read()
            f.close()
        except:
            print('Input gen TLE')
            exit(0)
        try:
            subprocess.run(["python3 " + code1 +  " > " + output1], input=inputString.encode(), timeout=tle, shell=True)
        except:
            print('Code1 TLE')
            exit(0)
        try:
            subprocess.run(["python3 " + code2 +  " > " + output2], input=inputString.encode(), timeout=tle, shell=True)
        except:
            print('Code2 TLE')
            exit(0)
            
        f = open(output1)
        outputResult1 = f.readlines()
        f.close()
        f = open(output2)
        outputResult2 = f.readlines()
        f.close()
        wrong = False
        if len(outputResult1) != len(outputResult2):
            wrong = True
        if not wrong:
            for i in range(len(outputResult1)):
                if outputResult1[i].strip() != outputResult2[i].strip():
                    wrong = True
                    break
        if wrong:
            print("Result mismatched")
            print('Input was',inputfile)
            print('Output1 was',output1)
            print('Output2 was',output2)
            exit(0)
