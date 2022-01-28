from operator import itemgetter
firstClass = [ 
{'name':"Bob", 'grade':94},
{'name':"Boe", 'grade':93},
{'name':"Vaa", 'grade':92},
{'name':"Vre", 'grade':91},
{'name':"Toe", 'grade':94},
]
secondClass = [
{'name':"Dan", 'grade':64},
{'name':"Don", 'grade':63},
{'name':"Tim", 'grade':76},
{'name':"Tom", 'grade':61},
{'name':"Sebastian Jr.", 'grade':74},
]
newlist = sorted(firstClass, key=itemgetter('grade'), reverse=True)
newlist1=sorted(secondClass, key=itemgetter('grade'), reverse=True)
#print(newlist[0]['grade'])
for i in range(1,len(newlist)):
    if newlist[0]['grade']>=75 and newlist[0]['grade']> newlist[i]['grade']:
       a=(newlist[0]['name'])
       break
    elif newlist[0]['grade']>=75 and newlist[0]['grade']==newlist[i]['grade']:
       a=((newlist[0]['name'])+ " "+newlist[i]['name'])
       break
    
for i in range(1,len(newlist1)):
    if newlist1[0]['grade']>=75 and newlist1[0]['grade']> newlist1[i]['grade']:
       b=(newlist1[0]['name'])
       break
    elif newlist1[0]['grade']>=75 and newlist1[0]['grade']==newlist1[i]['grade']:
       b=((newlist1[0]['name'])+" "+newlist1[i]['name'])  
       break     

print(a+" "+b)