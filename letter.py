vow = "aeiouAEIOU"
sum = 0
sum1 = 0
input1='baceb'
inpLen = len(input1)
for L in range(1, inpLen + 1):
    for i in range(inpLen - L + 1):
        j = i + L - 1
        for k in range(i, j + 1):
           # print(input1[k])
            if input1[k] in vow:
                sum =sum + 1
print( sum)


for L in range (inpLen):
        #print (input1[le])
        for  i in range(inpLen - L ):
            #print(input1[le1] )
            j = i + L - 1
            for k in range (i,j):
                print(input1[k])
                if input1[k] in vow:
                    sum1 =sum + 1

print (sum1)

#import itertools
#print(list(itertools.permutations(['b','a','c','e','b'])))