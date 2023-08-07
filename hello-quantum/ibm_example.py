#!/usr/bin/env python
# coding: utf-8

# In[2]:


from qiskit import *


# In[3]:


circuit = QuantumCircuit(2,2)


# In[4]:


circuit.draw()


# In[5]:


circuit.h(0)


# In[6]:


circuit.draw()


# In[7]:


circuit.cx(0, 1)
circuit.draw()


# In[8]:


circuit.measure([0, 1], [0, 1]) #mesure qubit 0 and 1, and associate to classical bits 0 and 1


# In[9]:


circuit.draw()


# In[10]:


simulator = Aer.get_backend("qasm_simulator")


# In[12]:


execute(circuit, backend=simulator).result()


# In[13]:


from qiskit.visualization import plot_histogram


# In[14]:


result = execute(circuit, backend=simulator).result()


# In[15]:


plot_histogram(result.get_counts(circuit))


# In[ ]:




