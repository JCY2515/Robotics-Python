# Chung Yin Wong
# Lab 1 Forward Kinematics via D-H method
##---------##
import numpy as np

# Input Variables
theta_1 = 45.0
theta_2 = 45.0
theta_3 = 45.0

# Know/Fixed Variables
a1 = 5.0 #link length a-1 in cm
a2 = 7.5 #link length a-2 in cm
a3 = 5.5
a4 = 7.5
a5 = 5.5
a6 = 5.0

##---------##
# D-H parameters (as variables)
alpha_1 = 0.0
alpha_2 = 0.0
alpha_3 = 0.0
r_1 = a2
r_2 = a4
r_3 = a6
d_1 = a1
d_2 = a3
d_3 = a5

#Convert Angle degrees to radians
thetaRad_1 = np.deg2rad(theta_1)
thetaRad_2 = np.deg2rad(theta_2)
thetaRad_3 = np.deg2rad(theta_3)

alphaRad_1 = np.deg2rad(alpha_1)
alphaRad_2 = np.deg2rad(alpha_2)
alphaRad_3 = np.deg2rad(alpha_3)
##D-H Parameters (as a matrix)
DH_ParmeterTable = [[thetaRad_1, alphaRad_1, r_1, d_1],
                    [thetaRad_2, alphaRad_2, r_2, d_2],
                    [thetaRad_3, alphaRad_3, r_3, d_3]]
print('D-H Parameters Table: ')
print(np.matrix(DH_ParmeterTable),'\n')
##---------##
# Creating Homogenous Matrices from D-H Parameter Table
DH_T = DH_ParmeterTable

i=0 #for the first row of the D-H Parmeter Table
H0_1 = [[np.cos(DH_T [i][0]), -np.sin(DH_T [i][0])*np.cos(DH_T [i][1]), np.sin(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.cos(DH_T [i][0])],
        [np.sin(DH_T [i][0]), np.cos(DH_T [i][0])*np.cos(DH_T [i][1]), -np.cos(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.sin(DH_T [i][0])],
        [0, np.sin(DH_T[i][1]), np.cos(DH_T [i][1]), (DH_T [i][3])],
        [0, 0, 0, 1]]

i=1 #for the second row of the D-H Parmeter Table
H1_2 = [[np.cos(DH_T [i][0]), -np.sin(DH_T [i][0])*np.cos(DH_T [i][1]), np.sin(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.cos(DH_T [i][0])],
        [np.sin(DH_T [i][0]), np.cos(DH_T [i][0])*np.cos(DH_T [i][1]), -np.cos(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.sin(DH_T [i][0])],
        [0, np.sin(DH_T[i][1]), np.cos(DH_T [i][1]), (DH_T [i][3])],
        [0, 0, 0, 1]]

i=2 #for the third row of the D-H Parmeter Table
H2_3 = [[np.cos(DH_T [i][0]), -np.sin(DH_T [i][0])*np.cos(DH_T [i][1]), np.sin(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.cos(DH_T [i][0])],
        [np.sin(DH_T [i][0]), np.cos(DH_T [i][0])*np.cos(DH_T [i][1]), -np.cos(DH_T[i][0])*np.sin(DH_T [i][1]), (DH_T [i][2])*np.sin(DH_T [i][0])],
        [0, np.sin(DH_T[i][1]), np.cos(DH_T [i][1]), (DH_T [i][3])],
        [0, 0, 0, 1]]

##---------##
H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)

print('Homogenoues Matrix from base to end: ')
np.set_printoptions(precision=3, suppress=True) # this is to print to three decimal places without scientific-notation
print(np.matrix(H0_3),'\n')
print('End-Effetor_X: %.3f' % H0_3[0][3])
print('End-Effetor_Y: %.4f' % H0_3[1][3])
print('End-Effetor_Z: %.2f' % H0_3[2][3])
