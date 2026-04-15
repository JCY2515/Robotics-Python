import numpy as np

##a1=5 #length of link a1 in cm
##a2=7 #length of line a2 in cm
##a3=5.5 #length of line a3 in cm
##a4=8 #length of line a4 in cm

d1=1
d2=1
d3=1

a1=1
a2=1
a3=1
a4=1

T1=30 #Theta 1 angle in degrees
T2=90 #Theta 2 angle in degress
T3=30 #Theta 3 angle in degrees
T4=90 #Theta 4 angle in degress
T5=30 #Theta 5 angle in degrees
T6=90 #Theta 6 angle in degress

T1=(T1/180)*np.pi #Theta 1 in radians
T2=(T2/180)*np.pi #Theta 2 in radians

PT=[[(90.0/180.0)*np.pi,(90.0/180.0)*np.pi,0,a1+d1],
    [(90.0/180.0)*np.pi,(-90.0/180.0)*np.pi,0,a2+d2],
    [0,0,0,a3+d3]]

i=0
H0_1=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0,0,0,1]]

i=1
H1_2=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0,0,0,1]]

i=2
H2_3=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0,0,0,1]]
print ("H0_1=")
print (np.matrix(H0_1))
print ("H1_2=")
print (np.matrix(H1_2))
print ("H2_3=")
print (np.matrix(H2_3))

H0_2=np.dot(H0_1,H1_2)
H0_3=np.dot(H0_2,H2_3)

print ("H0_3=")
print (np.matrix(H0_3))
##R0_1 = [[np.cos(T1),-np.sin(T1),0],[np.sin(T1),np.cos(T1),0],[0,0,1]]
##R1_2 = [[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]
##
##R0_2 = np.dot(R0_1,R1_2)
##
###print(np.matrix(R0_1))
##print("\n")
##
##d0_1 = [[a2*np.cos(T1)],[a2*np.sin(T1)],[a1]]
##d1_2 = [[a4*np.cos(T2)],[a4*np.sin(T2)],[a3]]
##
###print(np.matrix(d0_1))
##print("\n")
##
##H0_1=np.concatenate((R0_1,d0_1),1)
##H0_1=np.concatenate((H0_1,[[0,0,0,1]]),0)
##
###print(np.matrix(H0_1))
##
##H1_2=np.concatenate((R1_2,d1_2),1)
##H1_2=np.concatenate((H1_2,[[0,0,0,1]]),0)
##
##H0_2=np.dot(H0_1,H1_2)
##
##print(np.matrix(H0_2))
