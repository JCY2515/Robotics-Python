#Lab 03 – Decoupled Inverse Kinematics via Spherical Wrist
#Chung Yin Wong
import numpy as np

X=10.0
Y=3.0
Z=8.0

a1=6.0 #cm
a2=5.5
a3=5.5
a4=3.0
a5=a6=0.5 

Theta1=np.arctan2(Y,X)
Theta2=-np.arcsin((Z-a1)/a2)
Theta3=-np.arccos((Z-a1)/(a2+a3))

R0_6=[[1.0,0.0,0.0],
      [0.0,1.0,0.0],
      [0.0,0.0,1.0]]

R0_1=[[-np.cos(Theta1),0,-np.sin(Theta1)],
      [-np.sin(Theta1),0,np.cos(Theta1)],
      [0,1,0]]

R1_2=[[-np.cos(Theta2),np.sin(Theta2),0],
      [-np.sin(Theta2),-np.cos(Theta2),0],
      [0,0,1]]

R2_3=[[np.sin(Theta3),0,np.cos(Theta3)],
      [-np.cos(Theta3),0,np.sin(Theta3)],
      [0,-1,0]]

R0_3= np.dot(np.dot(R0_1,R1_2),R2_3) 

invR0_3=np.linalg.inv(R0_3)

R3_6=np.dot(invR0_3,R0_6)

print ("R3_6 = ",np.matrix(R3_6))

# R3_6[2][2] is cos(Theta5)
Theta5 = np.arccos(R3_6[2][2])
print("Theta5 =", Theta5, "radians")

# R3_6[2][0] is -sin(Theta5)*sin(Theta6), R3_6[2][1] is sin(Theta5)*cos(Theta6)
Theta6 = np.arctan2(-R3_6[2][0], R3_6[2][1])
print("Theta6 =", Theta6, "radians")

# R3_6[1][2] is sin(Theta4)*sin(Theta5), R3_6[0][2] is cos(Theta4)*sin(Theta5)
Theta4 = np.arctan2(R3_6[1][2], R3_6[0][2])
print("Theta4 =", Theta4, "radians")

R3_4=[[0,np.cos(Theta4),-np.sin(Theta4)],
      [0,np.sin(Theta4),np.cos(Theta4)],
      [1,0,0]]

R4_5=[[0,-np.sin(Theta5),np.cos(Theta5)],
      [0,np.cos(Theta5),np.sin(Theta5)],
      [-1,0,0]]

R5_6=[[np.cos(Theta6),-np.sin(Theta6),0],
      [np.sin(Theta6),-np.cos(Theta6),0],
      [0,0,1]]

R3_6 = np.dot(np.dot(R3_4,R4_5),R5_6)

# R3_6 = Ry(-Theta5) - a single Y-axis rotation
R3_6_Check = R3_6 

print("\nR3_6_Check = ",np.matrix(R3_6_Check))