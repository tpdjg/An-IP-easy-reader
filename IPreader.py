import os
import easygui
result=""
ipaddress = os.popen("ipconfig",'r')
nowturn=0
cfs=["",]
for line in ipaddress:
    if line[0]!="\n"and line[0]!=" ":
        cfs.append(line)
        nowturn+=1
        continue
    cfs[nowturn]+=line
for i in cfs:
    range(1,len(cfs))
nums=range(1,len(cfs)-1)
numsp=[]
for i in nums:
    numsp.append(str(i))
    if len(cfs[i+1])<=100:
        numsp[i-1]+=("              May Not connected")
    else:
        numsp[i-1]+=("              May Connected")
while True:
    a=easygui.choicebox("Windows IP Configuration"," easy IP reader",numsp)
    if a=="Cancel"or a==None:
        break
    else:
        counter=int(numsp.index(a))
        if easygui.msgbox(cfs[counter+2]," easy IP reader")==None:
            break
