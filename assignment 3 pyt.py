#!/usr/bin/env python
# coding: utf-8

# <h3>Q no 1:  Write a python program to find number of occurrences of given number in a list with out using built-in methods</h3>
# <h4>**1 generate a list of some random num which is repeated again and again</h4>
# <h4>**2 take user input any number</h4>
# <h4>**3 find the number of occurrences of that num in your list</h4>
# <h4>**4 print some message to user with that result</h4>

# In[1]:


random=[1,2,2,4,5,6,6,7,7,7,9,20]
number=0
num=int(input("Enter the Number : "))

for i in random : 
    if(num==i):
         number+=1
print("Your Number has been occured",number,"times")
            


# In[ ]:





# <h3>Q no 2:   ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# <br/><br/><br/><br/><br/>
# Write a python program to print website suffixes (com , org , net ,in) from this list
# 
# Hint : Use split() method to perform this task
# </h3>
# 

# In[2]:


web_sites = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
for i in web_sites:
    suff=i.split(".")[-1]
    print(suff)


# In[ ]:





# <h3> Q no 3 : Write a program which can compute the factorial of a given numbers.</h3>
# <br/>
# <br/>
# <h4>**1 first take user input any number</h4>
# <h4>**2 calculate factorial of that input and then print the result to user</h4>

# In[3]:


number=int(input("Enter the number : "))
factorial=1
if number<0:
    print("not possible")
elif number==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,number+1):
        factorial = factorial*i
    print("Factorial of ",number," = ",factorial)


# In[ ]:





# In[ ]:





# In[ ]:





# <h3>Q 4 (a) :  If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.</h3>

# In[4]:


Persons = ['Farrukh','Rao','Asad','Umair']
for i in Persons:
    print(i,"! You are invited on Dinner by Taha Jamal Tomorrow.")


# In[ ]:





# In[ ]:





# <h3>Q 4 (b) : You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.<br/></br><br/>
# •	 Start with your program from Q 4 (a). Add a print statement at the
# end of your program stating the name of the guest who can’t make it.<br/></br><br/>
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.<br/></br><br/>
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.<br/></br><br/></h3>

# In[5]:


print(Persons[2]," Cannot make dinner")
Persons[Persons.index("Asad")]= "Usama"


# In[6]:


Persons


# In[7]:


for i in Persons:
    print(i,"! You are invited on Dinner by Taha Jamal Tomorrow.")


# <h3>Q 4 (c) : You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.<br/></br><br/>
# •	 Start with your program from Q 4 (a) and (b) Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.<br/></br><br/>
# •	 Use insert() to add one new guest to the beginning of your list.<br/></br><br/>
# •	 Use insert() to add one new guest to the middle of your list.<br/></br><br/>
# •	 Use append() to add one new guest to the end of your list.<br/></br><br/>
# •	 Print a new set of invitation messages, one for each person in your list.<br/></br><br/></h3>

# In[8]:


for i in Persons:
    print(i,"! I have found a bigger dinner table")


# In[9]:


Persons.insert(0,'Hamdan')
Persons.insert(3,'Rameez')
Persons.append('Umar')


# In[10]:


for i in Persons:
    print(i,"! You are invited on Dinner by Taha Jamal Tomorrow.")


# <h5> Q 5 : Here you have some data in variable below, your task is to make a list of specific word Surah then print the list and length of list</h5>
# 

# In[11]:


line = "Surah I Who believe in the Unseen, Surah Are steadfast in prayer, And spend Surah out of what We Have provided for them;"
data = line.split(" ")
listt = []
for i in data:
    if i == 'Surah':
        listt.append(i)
print(listt)
print("The word ",listt[0]," appears ",len(listt)," times in the given sentence.")


# In[ ]:





#  <h3>Q no 6 : You have some name of cities in list named cities, Your task is to check whether Karachi is present in this list or not, if present print the index where the value Karachi is present</h3>

# In[12]:


cities = ["Lahore","karachi","Islamabad","Peshawar","Quetta"]


# In[53]:


for i in cities:
    if(i == 'Karachi'):
         print("The Karachi is at index ",cities.index(i))
 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




