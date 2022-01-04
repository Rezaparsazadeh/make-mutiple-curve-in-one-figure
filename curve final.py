#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns 
import sklearn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


clay=pd.read_excel(r"C:\Users\asus\Desktop\HW-2c1.xlsx")


# In[ ]:





# In[9]:


clay


# In[10]:


pota=clay[['POTA(%)']]
thor=clay[['THOR(PPM)']]
ax=plt.subplot(1,1,1)


a1=np.array([0,0.72])
b1=np.array([0,20])
z1=plt.plot(a1,b1,label="heavy minerals")

a1=np.array([0,1.55])
b=np.array([0,19.64])
plt.plot(a1,b,label="kaolinite")

ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')

#ax.text(0.8,1,'kaolinite')


a=np.array([0,6.71])
b=np.array([0,21.14])
plt.plot(a,b,label="monttmorillonite")

ax.fill_between([0 , 1.55] , [0 , 20] , [0 , 5.4],color='goldenrod')
ax.fill_between([1.55 , 6.4] , [20, 20] , [5.4, 20],color='goldenrod')

#ax.text(3,10,'monttmorillonite')

a=np.array([0,4.26])
b=np.array([0,8.89])
plt.plot(a,b,label="illite")

ax.fill_between([0 , 4.26] , [0 , 13.7] , [0 , 8.89],color='orange')

#ax.text(0.5,6,'illite')

a=np.array([0,4.22])
b=np.array([0,6.52])
plt.plot(a,b,label="micas")

ax.fill_between([0 , 4.22] , [0 , 8.89] , [0 , 6.52],color='green')

#ax.text(0.6,6,'mica')

a=np.array([0,4.26])
b=np.array([0,3.48])
plt.plot(a,b,label='glauconite')


ax.fill_between([0 , 4.26] , [0 , 6] , [0 , 3.48],color='yellow')
#ax.text(0.5,6,'illite')
#ax.text(0.4,3,'feldspar')


a=np.array([0,4.298])
b=np.array([0,2.6])
plt.plot(a,b,label='feldspar')

ax.fill_between([0 , 4.298] , [0 , 3.33] , [0 , 2.6],color='pink')



a=np.array([0,4.298])
b=np.array([0,0])
plt.plot(a,b,label='feldspar')

ax.fill_between([0,4.298],[0,3.33],[0,0],color='pink')



plt.scatter(pota,thor,s=1,color='r' ) 


ax.text(-0.2 , 5,'heavy mineral', rotation=80)
ax.text(0.6 , 17,'kaolinite', rotation=20)
ax.text(0.7, 6,'montmorillonite', rotation=50)
ax.text(3 , 8,'illite', rotation=35)
ax.text(3, 5,'micas', rotation=20)
ax.text(2,2 ,'glauconite', rotation=10)
ax.text(3 , 1,'feldspar', rotation=0)


plt.xlabel("K(%)")
plt.ylabel("TH(ppm)")
plt.title("Mineral identification")


plt.show()


# In[11]:



ax=plt.subplot(1,1,1)
ax.set_xscale('log')

#k-feldspar
plt.plot([0.8,1.1],[9.5,9.5])
plt.plot([1.1,1.1],[9.5,8.7])
plt.plot([1.1,0.8],[8.7,8.7])
plt.plot([0.8,0.8],[8.7,9.5])

#glagconite 
plt.plot([0.8,1.5],[8,8])
plt.plot([1.5,1.5],[8,7.3])
plt.plot([1.5,0.8],[7.3,7.3])
plt.plot([0.8,0.8],[7.3,8])

#muscovite & lllite

plt.plot([1.5,4],[6.6,6.6],)
plt.plot([4,4],[6.6,5.9])
plt.plot([4,1.5],[5.9,5.9])
plt.plot([1.5,1.5],[5.9,6.6],)


#Interstratifiedmuscovite &lllite 
plt.plot([4,10],[5.3,5.3])
plt.plot([10,10],[5.3,4.5])
plt.plot([10,4],[4.5,4.5])
plt.plot([4,4],[4.5,5.3])


#kaolinite & cholorite
plt.plot([10,30],[3.83,3.83])
plt.plot([30,30],[3.83,3.006])
plt.plot([30,10],[3.006,3.006])
plt.plot([10,10],[3.006,3.83])



#bauxite
plt.plot([30,100],[2.4,2.4])
plt.plot([100,100],[2.4,1.6])
plt.plot([100,30],[1.6,1.6])
plt.plot([30,30],[1.6,2.4])







ax.text(0.7 ,9.6,'k-feldspar', rotation=0)
ax.text(0.7 , 8.2,'glagconite', rotation=0)
ax.text(1.5,7,'muscovite & lllite', rotation=0)
ax.text(2.5 , 5.4,'Interstratifiedmuscovite &lllite', rotation=0)
ax.text(9.3, 4.1,'kaolinite & cholorite', rotation=0)
ax.text(39, 2.6,'bauxite', rotation=0)






plt.show()


# In[ ]:





# In[ ]:





# In[12]:


clay1=clay.copy()


# In[13]:


ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')ax.fill_between([0 , 0.72] , [0 , 19.64] , [0 , 8.70],color='gold')
ax.fill_between([0.7 , 1.55] , [19.64, 20] , [8 , 20],color='gold')


# In[ ]:


type(clay1)


# In[14]:


type(x)


# In[15]:


type(y)


# In[ ]:





# In[16]:


x=clay1[['THOR(PPM)/POTA(%)']].values
y=clay1[['PEF(B/E)']].values
y=np.array(y)
x[x<0]=1
y[y<0]=1
ax=plt.subplot(1,1,1)
ax.set_xscale('log')


plt.plot([0.8,1.7],[7.24919,7.24919])
plt.plot([1.7,1.7],[7.24919,5.3398])
plt.plot([1.7,0.8],[5.3398,5.3398])
plt.plot([0.8,0.8],[5.3398,7.24919])

#Biotite 
plt.plot([1.9,3.5],[6.4689,6.4689])
plt.plot([3.5,3.5],[6.4689,6.13121])
plt.plot([3.5,1.9],[6.13121,6.13121])
plt.plot([1.9,1.9],[6.13121,6.4689])

#chlorite

plt.plot([10,33],[6.37097,6.37097],)
plt.plot([33,33],[6.37097,6.02903])
plt.plot([33,10],[6.02903,6.02903])
plt.plot([10,10],[6.02903,6.37097],)


#feldespars
plt.plot([0.45,1.5],[3.17742,3.17742])
plt.plot([1.5,1.5],[3.17742,2.77419])
plt.plot([1.5,0.45],[2.77419,2.77419])
plt.plot([0.45,0.45],[2.77419,3.17742])


#moscoovit
plt.plot([1.9,3.5],[2.4152,2.4152])
plt.plot([3.5,3.5],[2.4152,2.04761])
plt.plot([3.5,1.9],[2.04761,2.04761])
plt.plot([1.9,1.9],[2.04761,2.4152])



#illite
plt.plot([2.5,6],[3.410099,3.410099])
plt.plot([6,6],[3.410099,3.68862])
plt.plot([6,2.5],[3.68862,3.68862])
plt.plot([2.5,2.5],[3.68862,3.410099])



#mixed clays
plt.plot([5.5,10.1],[3.8505,3.8505])
plt.plot([10.1,10.1],[3.8505,2.29611])
plt.plot([10.1,5.5],[2.29611,2.29611])
plt.plot([5.5,5.5],[2.29611,3.8505])

#montmorllite
plt.plot([5.5,10.1],[2.00284,2.00284])
plt.plot([10.1,10.1],[2.00284,2.26214])
plt.plot([10.1,5.5],[2.26214,2.26214])
plt.plot([5.5,5.5],[2.26214,2.00284])

#kaolonite
plt.plot([10,30],[1.84224,1.84224])
plt.plot([30,30],[1.84224,1.59897])
plt.plot([30,10],[1.59897,1.59897])
plt.plot([10,10],[1.59897,1.84224])


plt.scatter(x,y,s=0.08,color='r' )



ax.text(0.3 ,3.3,'feldespars', rotation=0)
ax.text(1.9 , 6.8,'Biotite', rotation=0)
ax.text(10,6.5,'chlorite', rotation=0)
ax.text(0.5 , 7.4,'glauconite', rotation=0)
ax.text(0.8, 3.8,'moscoovit', rotation=0)
ax.text(1.6, 2.6,'illite', rotation=0)
ax.text(4.6,4,'mixed clays', rotation=0)
ax.text(4.5,1.9 ,'montmorllite', rotation=0)
ax.text(9,1.4,'kaolonite', rotation=0)

plt.xlabel("Th(ppm)/K(%)")
plt.ylabel("pe(ppm)")
plt.title("Clay type determination")




plt.show()


# In[ ]:





# In[ ]:




