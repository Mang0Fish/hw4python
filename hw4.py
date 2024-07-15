#Starting from section 2
#True True True True False True False True True True False True True False False False True True False True

#Section 3 + Bonus
temp = float(input("Enter temperature"))
tempIf = "Hot" if temp > 30 else ("Freezing" if temp < 0 else "Normal")
print(tempIf)

#Section 4
g = int(9)
for i in range(11):
    g += 1
    print(g)
    
g = 8
for i in range (6):
    g += 2
    print(g)
    
skip = int(input("Enter skip"))
g = int(10 - skip)
for i in range((10 // skip) + 1):
    g += skip
    print(g) 

sPnt = int(input("Enter start point"))
ePnt = int(input("Enter end point"))
skip = int(input("Enter gap"))

g = sPnt - skip
for i in range(((ePnt-sPnt) // skip)+1):
    g += skip
    print(g)

#Section 5 + Bonus
lst1=[]
i = int(0)
b = True 
sum = int(0)
while b:
    iq = int(input("Enter iq"))
    if iq > 30 and iq<300:            
        lst1.append(iq)
        sum += iq
        i += 1
    else:
        b = False
oldAvg = sum/i
print(oldAvg)
lst1Min = min(lst1)  
lst1Max = max(lst1)  
print(f"Lowest {lst1Min} Highest {lst1Max}")
print("one year of python training has been completed…")
lst2 =[]
i = int(0)
b = True 
sum = int(0)
while b:
    iq = int(input("Enter iq"))
    if iq > 30 and iq<300:            
        lst2.append(iq)
        sum += iq
        i += 1
    else:
        b = False
newAvg = sum/i
print(newAvg)
print(newAvg-oldAvg)
lst2Min = min(lst2)  
lst2Max = max(lst2)  
print(f"Lowest {lst2Min} Highest {lst2Max}")
if lst2Min < lst1Min:
    allMin = lst2Min
else:
    allMin = lst1Min
if lst2Max > lst2Min:
    allMax = lst2Max
else:
    allMax = lst1Max
print(f"Overall highest {allMax}, Overall lowest {allMin}")
#Section 6 + Bonus
str3 = ""
while True:
    str1 = str(input("Enter string 1"))
    str2 = str(input("Enter string 2"))
    if str1 != str2:
        print(str1+' '+str2)
        str3 += str1+' '+str2+' '
    else:
        print(str3)#I know it wasnt requested
        break














