#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1

v = "message"
print(v)


# In[4]:


# Task 2: Quote

Quote = '“A person who never made a mistake never tried anything new.”'
print("Albert Einstein once said, ", Quote)


# In[13]:


# Task 3: Area of Circle

x = float(input("Input Radius: "))
y = 3.142 * (x * x)

print("Area of Circle with radius ", x, "is ", y)


# In[20]:


# Task 4: Number tester

x = int(input("Enter number: "))

if x < 0:
    print("Number is negative")
elif x == 0:
    print("Number is zero")
else:
    print("Number is positive")
        
        


# In[6]:


# Task 5 Vowel tester

vowels = ["A", "E" , "I" , "O" , "U" , "a", "e", "i", "o", "u"]
letter = input("Enter a character: ")
if letter in vowels:
    print("Letter " + letter + " is Vowel")
else:
    print("Letter " + letter + " is not Vowel")


# In[8]:


# Task 6: BMI Calculator

height = int(input("Enter Height in Cm: "))
weight = int(input("Enter Wegiht in Kg: "))

height_in_m = height/100
bmi = weight / (height_in_m * height_in_m)
bmi = str(bmi)


print("Your BMI is " + bmi)


# In[11]:


# Task 7: List of friend's name 

names = ["safi", "bilal", "ali", "tabish", "junaid"]
for a_friend_name in names:
    print(a_friend_name)


# In[13]:


# Task 7: List of friend's name with personalized message

names = ["safi", "bilal", "ali", "tabish", "junaid"]
for a_friend_name in names:
    print("Hi " + a_friend_name + ", you are a good friend.")


# In[20]:


# Task 8: Nine favourite dishes

foods = ["biryani" , "nihari" , "paaya" , "haleem" , "pulao" , "daal chawal" , "brain masala" , "karhaai" , "tikka"]

print("The first three items in the list are: " , foods[:3])
print("Three items from the middle of the list are: " , foods[3:6])
print("The last three items in the list are: " , foods[6:])


# In[34]:


# Task 9 

foods = ["biryani" , "nihari" , "paaya" , "haleem" , "pulao" , "daal chawal" , "brain masala" , "karhaai" , "tikka"]
friend_foods = ["biryani" , "nihari" , "paaya" , "haleem" , "pulao" , "daal chawal" , "brain masala" , "karhaai" , "tikka"]

foods.insert(0,"pizza")
friend_foods.insert(0,"burger")

print(foods)
print(friend_foods)

for my_fav_foods in foods:
    print("My favorite foods are",my_fav_foods)
    
for friend_fav_foods in friend_foods:
    print("My friend's favorite foods are", friend_fav_foods)


# In[ ]:




