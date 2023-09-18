#!/usr/bin/env python
# coding: utf-8

# # OPERADORE DE ASIGNACION

# In[1]:


numero=5
numero=numero+3
print(numero)


# In[2]:


numero=5
numero+=3
print(numero)


# In[3]:


numero=5
numero=numero**3
print(numero)


# In[4]:


numero=5
numero**=3
print(numero)


# # OPERADORE DE COMPARACION 

# In[5]:


numero1=5
numero2=4
numero1==numero2


# In[6]:


nombre1="roxana"
nombre2="rouss"
nombre1==nombre2


# In[7]:


numero1=6
numero2=12
numero3=8
numero1<numero2


# In[8]:


numero1<numero2


# In[9]:


numero3<numero1


# In[10]:


not(numero1<numero2)


# In[11]:


numero1<numero2 and numero3<numero1


# In[13]:


aula =["juan","jesu","marlon"]
alumno1="diego"
alumno2="juan"


# In[14]:


#diego eta en el aula?
alumno1 in aula


# In[15]:


alumno2 in aula


# In[16]:


alumno2 not in aula


# # OPERADORE DE IDENTIDAD

# In[23]:


aula1 =["juan","jesu","marlon"]
aula2 =["juan","jesu","marlonnn"]
aula3=aula1


# In[19]:


aula3 is aula1#aula 3 comparte el mismo objeto que aula 1 ?


# In[20]:


print(aula1)


# In[21]:


print(aula3)


# In[24]:


print(aula2)


# In[ ]:




