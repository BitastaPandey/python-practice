import statistics

student=input("Please provide the no of students followed by their numbers: ")
print(student)

list = student.split(" ")
print(list)

while len(list)!=int(list[0])+1:
    student1=input("Please provide the no of students followed by their numbers: ")
    list =student1.split(" ")

# 
for i in range(1,len(list)):
  
  if (int(list[i])>100 or int(list[i])<0):
    
    list[i]=input(f"Please provide {i} no of student's  correct number")
    while int(list[i])>100 or int(list[i])<0:
      
      list[i]=input(f"Please provide {i} no of student's  correct number")
print(list)

            
score=list[1:len(list)] 
n=len(score)
score_list=[]  
for i in range(n):
    # score_list[i]=int(score[i])
    score_list.append(int(score[i]))


print(score_list)   
average=statistics.mean(score_list) 

highest_number=0
for i in range(1,len(list)):
    if int(list[i])>average :
        highest_number=highest_number+1
average_number=highest_number/int(list[0])*100
average_number=format(average_number,".3f")
print(str(average_number)+"%")
        
      


