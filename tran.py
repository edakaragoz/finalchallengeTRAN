
"""
Rosalind - TRAN Solution
Problem url : https://rosalind.info/problems/tran/
Ege University
Bioengineering
Biyomühendislik için Biyoinformatik
Group 8
"""

#Problem : Transitions and Transversions
#Given Two DNA strings ts and tv of equal length (at most 1 kbp).
#Return The transitiontransversion ratio R(ts,tv).

import os

def R(ts,tv):
    tsCounter = 0
    tvCounter = 0
    for i in range(0, len(ts)):
        if (ts[i] != tv[i]):
            if (ts[i] == 'A' and tv[i] == 'G'):
                tsCounter = tsCounter + 1
            elif (ts[i] == 'G' and tv[i] == 'A'):
                tsCounter = tsCounter + 1
            elif (ts[i] == 'C' and tv[i] == 'T'):
                tsCounter = tsCounter + 1
            elif (ts[i] == 'T' and tv[i] == 'C'):
                tsCounter = tsCounter + 1
            else:
                tvCounter = tvCounter + 1
    print("Transitiontransversion ratio R(ts,tv) : ", tsCounter/tvCounter)
    
file = open("dataset.txt")
print("dataset.txt file opened.")

fileData = file.read()
fileData = fileData.replace("Rosalind_", "")
fileData = fileData.replace("\n", "")
fileData = ''.join([i for i in fileData if not i.isdigit()])

tt = fileData.split(">")
ts = tt[1]
tv = tt[2]

R(ts,tv)
os.system('pause')
