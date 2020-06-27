a=input()
print(a)

#list comprehension: 
try1=input()        #1 2 3 4 5
try1=try1.split()
print(try1)

try2=[int(x) for x in try1]
print(try2)

#Dictionary: 

dict1={1:"Surabhi<3",'two':"dhruv",3:"manoj<3",4:"Sid<3"};
print(dict1['two'])

#function:
def summ(numbers):
    sum1=0;
    for i in numbers: 
        sum1=sum1+i;
    print("Sum is: ", sum1);
    
numbers=[1,2,3,4]
summ(numbers);