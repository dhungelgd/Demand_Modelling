# -*- coding: utf-8 -*-

#%% Definition of the inputs
'''
Input data definition 
'''


from ramp.core.core import User, np
User_list = []

'''
This example input file represents an whole village-scale community,
adapted from the data used for the Journal publication. It should provide a 
complete guidance to most of the possibilities ensured by RAMP for inputs definition,
including specific modular duty cycles and cooking cycles. 
For examples related to "thermal loads", see the "input_file_2".
'''

#Create new user classes
P3_UHI = User("high income",50)
User_list.append(P3_UHI)

#Create new appliances

'''
P3_UHI_Rice_Cooker = P3_UHI.Appliance(P3_UHI,1,450,1,960,0,30, 'no',3)
P3_UHI_Rice_Cooker.windows([300,1260],[0,0])
P3_UHI_Rice_Cooker.specific_cycle_1(360,180,90,120)
P3_UHI_Rice_Cooker.specific_cycle_2(225,180,90,0)
P3_UHI_Rice_Cooker.specific_cycle_3(360,240,90,180)
P3_UHI_Rice_Cooker.cycle_behaviour([300,540],[540,660],[660,840],[0,0],[840,1080],[1080,1260])
'''
'''
P3_UHI_Rice_Cooker = P3_UHI.Appliance(P3_UHI,1,450,1,1440,0,30, 'no',3)
P3_UHI_Rice_Cooker.windows([0,1440],[0,0])
P3_UHI_Rice_Cooker.specific_cycle_1(50,300,450,360)
P3_UHI_Rice_Cooker.specific_cycle_2(500,180,100,240)
P3_UHI_Rice_Cooker.specific_cycle_3(450,180,50,180)
P3_UHI_Rice_Cooker.cycle_behaviour([0,300],[300,660],[660,840],[840,1080],[1080,1260],[1260,1440])
'''

P3_UHI_Rice_Cooker = P3_UHI.Appliance(P3_UHI,1,450,1,1440,0.8,30, 'no',3)
P3_UHI_Rice_Cooker.windows([0,1440],[0,0])
P3_UHI_Rice_Cooker.specific_cycle_1(50,300)
P3_UHI_Rice_Cooker.specific_cycle_2(350,540,300,420)
P3_UHI_Rice_Cooker.specific_cycle_3(50,180)
P3_UHI_Rice_Cooker.cycle_behaviour([0,300],[0,0],[300,840],[840,1260],[1260,1440],[0,0])

P3_UHI_Air_Conditioner = P3_UHI.Appliance(P3_UHI,1,1000,1,1440,0,30, 'no',3)
P3_UHI_Air_Conditioner.windows([0,1440],[0,0])
P3_UHI_Air_Conditioner.specific_cycle_1(700,240,200,180)
P3_UHI_Air_Conditioner.specific_cycle_2(150,300,500,180)
P3_UHI_Air_Conditioner.specific_cycle_3(150,240,700,300)
P3_UHI_Air_Conditioner.cycle_behaviour([0,240],[240,420],[420,720],[720,900],[900,1140],[1140,1440])