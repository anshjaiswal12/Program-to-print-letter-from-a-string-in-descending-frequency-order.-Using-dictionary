import operator #importing operator library
def most_frequent(string): #Creating function called 'most frequent' and caling string parameter
    d=dict() #creating a dictionary called 'd'
    for i in string: #using loop to storing every element in the  'string'
        if i not in d: #checking if the element stored in 'i' already present in dictionary in d
            d[i]=1 #if its not in d then then it will assign 1 to the frequeny
        else: #if the element is already there it means if its has been already asigned 1 once then
            d[i]+=1 #this will increase the frequency of it
    new=d #created a new dictionary called 'new'
    sorted_d=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True)) #sorted it in descending order
    for key, value in sorted_d.items(): #accessing keys and values in new variable called 'sorted_d'
        print(key,"=",value) #printing it
inp_f=input("Please enter a string:") #inputing the string
inp=inp_f.lower() #converting all elements in lower case
print(most_frequent(inp)) #calling the function
