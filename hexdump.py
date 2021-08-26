import sys

f=open(sys.argv[1],"rb")
file=list(f.read())
f.close()
file.append(0)

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
            for j in curr:
                buff_hex=buff_hex+hex(j)+'\t'
            buff_str='|'
            for j in curr:
                buff_str=buff_str+chr(j)
            buff_str=buff_str+'|'
            buffer.append(hex(count-16)+'\t'+buff_hex+buff_str)
        prev=curr
        curr=list()
    count=count+1
    curr.append(i)
buffer.append(hex(count-1))

for i in buffer:
    print(i)