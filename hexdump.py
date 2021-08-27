#Copyright(C)2021
#Made by Akihiro
#Version 2.0

import sys

f=open(sys.argv[1],"rb")
file=list(f.read())
f.close()
file.append(0) #file terminator

prev=list()
curr=list()
count=0
buffer=list()

for i in file:
    if(count!=0 and count%16==0):
        if(prev==curr):
            if(buffer[len(buffer)-1]=='*'):
                None
            else:
                buffer.append('*')
        else:
            buff_hex=''
            for j in range(0,len(curr)):
                space=''
                if(j!=0 and (j+1)%8==0):
                    space='  '
                else:
                    space=' '
                buff_hex=buff_hex+'00'[:-len(hex(curr[j])[2:])]+hex(curr[j])[2:]+space #hex fomatting
            buff_str='|'
            for j in curr: #string formatting
                if(j>31 and j<127):
                    buff_str=buff_str+chr(j)
                else:
                    buff_str=buff_str+'.' 
            buff_str=buff_str+'|'
            buffer.append('00000000'[:-len(hex(count-16)[2:])]+hex(count-16)[2:]+'  '+buff_hex+buff_str) #adding to buffer
        prev=curr
        curr=list()
    count=count+1
    curr.append(i)
buffer.append('00000000'[:-len(hex(count-16)[2:])]+hex(count-1)[2:])

print()
for i in buffer:
    print(i)