def padindrom(str1,str2):
    while len(str1)>=1 and len(str2)>=1:
          if len(str1)!=len(str2):
              return 0
          else:
              if len(str1)==1 and len(str2)==1:
                    if str1==str2:
                        return 1
                    else:
                        return 0    
              elif str1[0]==str2[-1]:
                    return padindrom(str1[1:],str2[:-1])
              else:
                    return 0                            
low=100*100
high=999*999
a=[]
for k in range(low,high):
    str1=str(k)
    if padindrom(str1,str1)==1:
        a.append(k)
temp=0        
for i in a:
    for j in range(100,999):
        if i%j==0:
            if i/j<=999:
               temp=i
               if temp<i:
                   temp=i
print "so lon nhat la",temp 
