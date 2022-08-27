#!/usr/bin/env python
# coding: utf-8

# In[23]:


# roll_num_123 name, class , mark

student_123 = {"name" : "hamza" , "class" : "intermediate" , "marks" : 77}
print(student_123["marks"])


# In[21]:


# roll_num_123 name, class , 4 marks

student_123 = {"name" : "hamza" , "class" : "intermediate" , "marks" : [77, 83, 90, 72]}
print(student_123["marks"])


# In[1]:


# roll_num_123 name, class , 4 marks, quiz 1, quiz 2, mid, final

student_123 = {"name" : "hamza" , 
               "class" : "intermediate" , 
               "marks" : 
                        {"quiz1" : 40 ,  
                        "quiz2" : 45 , 
                        "mid" : 50 ,
                        "final" : 55}}

subject_marks = input("Enter quiz number: ")
print(student_123["marks"][subject_marks])


# In[5]:


# roll_num_123 name, class , 4 marks, quiz 1, quiz 2, mid, final

student_123 = {"name" : "hamza" , 
               "class" : "intermediate" , 
               "marks" : 
                        {"quiz1" : 40 ,  
                        "quiz2" : 45 , 
                        "mid" : 50 ,
                        "final" : 55}}

exam_name = input("Enter exam: ")
only_marks = student_123["marks"]

print(only_marks[exam_name])


# In[12]:


# 10 students, 2 classes, 4 exams, 3 attempts allowed, take student name and exam_name as input
# show in which class the student get maximum marks

students = []
class1={"name":"AI", "marks": {"quiz1":40, "quiz2":45, "mid":50, "final":55}}
class2={"name":"CNC", "marks": {"quiz1":41, "quiz2":46, "mid":52, "final":56}}

student_1001 = {"name":"arif" , "class_AI":class1, "class_CNC":class2}
students.append(student_1001)
print(students)


# In[27]:


customer_29876 = {
"first name": "David",
"last name": "Elliott",
"address": "4803 Wellesley St.",
"discounts": ["brother_in_law", "standard", "volume", "loyalty"]
}

discount_amount = 0

if "brother_in_law" in customer_29876["discounts"]:
    discount_amount += .30
if "loyalty" in customer_29876["discounts"]:
    discount_amount += .15
if "volume" in customer_29876["discounts"]:
    discount_amount += .10
if "standard" in customer_29876["discounts"]:
    discount_amount += .05
    
print(discount_amount)


# In[ ]:


assignment: exericse 40 screenshot 

