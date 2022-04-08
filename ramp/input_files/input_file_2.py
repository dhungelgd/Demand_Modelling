# -*- coding: utf-8 -*-

#%% Definition of the inputs
"""
Input data for Ambon city, Indonesia
Month = February
"""

from ramp.core.core import User, np
User_list = []

#Create new user classes
P1_RLI = User("low income households",10) #10412
User_list.append(P1_RLI)

P1_ULI = User("residential shanty",12) #12280
User_list.append(P1_ULI)

P2_RMI = User("rural middle income households 1",19) #19530 = 10614 + 8916
User_list.append(P2_RMI)

P3_UHI = User("urban high income households",29)#3534 + 25652 = 29186
User_list.append(P3_UHI)

P4_UMI = User("urban middle income old households",15)#15057
User_list.append(P4_UMI)

P5_UMIX = User("residential and office",1) #897
User_list.append(P5_UMIX)

#Prototype 1 :rural low income households
P1_RLI_lamp = P1_RLI.Appliance(P1_RLI,2,60,2,360,0.2,10,wd_we_type = 2)
P1_RLI_lamp.windows([19*60,24*60],[6*60,8*60],0.35)

P1_RLI_fan = P1_RLI.Appliance(P1_RLI,1,75,3,720,0.2,15)
P1_RLI_fan.windows([20*60,24*60],[0,6*60+30],0.35,[11*60+30,15*60])

P1_RLI_TV = P1_RLI.Appliance(P1_RLI,1,120,2,360,0.1,30)
P1_RLI_TV.windows([11*60,15*60],[18*60,24*60],0.35)

P1_RLI_Phone_charger = P1_RLI.Appliance(P1_RLI,2,5,3,180,0.4,30)
P1_RLI_Phone_charger.windows([6*60+30,7*60+30],[14*60,15*60],0.35,[18*60,20*60])

#Prototype 1a : reidential shantys: urban low income households
P1_ULI_lamp = P1_ULI.Appliance(P1_ULI,2,60,2,360,0.2,10,wd_we_type = 2)
P1_ULI_lamp.windows([19*60,24*60],[6*60,8*60],0.35)

P1_ULI_fan = P1_ULI.Appliance(P1_ULI,1,75,3,720,0.2,15)
P1_ULI_fan.windows([20*60,24*60],[0,6*60+30],0.35,[11*60+30,15*60])

P1_ULI_TV = P1_ULI.Appliance(P1_ULI,1,120,2,360,0.1,30)
P1_ULI_TV.windows([11*60,15*60],[18*60,24*60],0.35)

P1_ULI_Phone_charger = P1_ULI.Appliance(P1_ULI,2,5,3,180,0.4,30)
P1_ULI_Phone_charger.windows([6*60+30,7*60+30],[14*60,15*60],0.35,[18*60,20*60])

P1_ULI_Rice_Cooker = P1_ULI.Appliance(P1_ULI,1,80,2,120,0.2,30)
P1_ULI_Rice_Cooker.windows([12*60,14*60],[19*60,21*60],0.35)
#
#Prototype 2 : Middle income houses
P2_RMI_lamp = P2_RMI.Appliance(P2_RMI,6,15,2,360,0.2,10,wd_we_type = 2)
P2_RMI_lamp.windows([18*60,24*60],[6*60,7*60],0.35)

P2_RMI_fan = P2_RMI.Appliance(P2_RMI,2,75,3,720,0.2,15)
P2_RMI_fan.windows([20*60,24*60],[0,6*60+30],0.35,[11*60+30,15*60])

P2_RMI_TV = P2_RMI.Appliance(P2_RMI,1,120,2,420,0.1,30)
P2_RMI_TV.windows([12*60,16*60],[19*60,23*60],0.35)

P2_RMI_Phone_charger = P2_RMI.Appliance(P2_RMI,4,5,3,180,0.4,60)
P2_RMI_Phone_charger.windows([6*60+30,7*60+30],[14*60,15*60],0.35,[18*60,20*60])

P2_RMI_Rice_Cooker = P2_RMI.Appliance(P2_RMI,1,80,2,180,0.2,30)
P2_RMI_Rice_Cooker.windows([11*60,13*60],[19*60,21*60],0.35)

P2_RMI_Fridge = P2_RMI.Appliance(P2_RMI,1,200,1,1440,0,30, 'yes',3)
P2_RMI_Fridge.windows([0,1440],[0,0])
P2_RMI_Fridge.specific_cycle_1(200,20,5,10)
P2_RMI_Fridge.specific_cycle_2(200,15,5,15)
P2_RMI_Fridge.specific_cycle_3(200,10,5,20)
P2_RMI_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

P2_RMI_laptop_wd = P2_RMI.Appliance(P2_RMI,1,120,1,120,0.2,120,wd_we_type = 0)
P2_RMI_laptop_wd.windows([17*60,22*60],[0,0],0.35)

P2_RMI_laptop_we = P2_RMI.Appliance(P2_RMI,1,120,3,240,0.2,120,wd_we_type = 1)
P2_RMI_laptop_we.windows([10*60,11*60+30],[14*60,14*60+30],0.35,[18*60,22*60])

P2_RMI_Hand_Mixer = P2_RMI.Appliance(P2_RMI,1,300,2,5,0.1,30,occasional_use = 0.5)
P2_RMI_Hand_Mixer.windows([12*60,13*60],[19*60,20*60],0.35)

P2_RMI_Iron = P2_RMI.Appliance(P2_RMI,1,300,2,60,0.2,15,occasional_use = 0.1)
P2_RMI_Iron.windows([10*60,11*60],[15*60,17*60],0.35)

P2_RMI_Toaster = P2_RMI.Appliance(P2_RMI,1,1000,1,5,0.2,5,occasional_use = 0.5)
P2_RMI_Toaster.windows([8*60,9*60],[0,0],0.35)

#Prototype 3 : Urban high income houses
P3_UHI_lamp = P3_UHI.Appliance(P3_UHI,6,15,2,360,0.2,10,wd_we_type = 2)
P3_UHI_lamp.windows([6*60,7*60],[18*60,24*60],0.35)

P3_UHI_fan = P3_UHI.Appliance(P3_UHI,2,75,2,240,0.2,15)
P3_UHI_fan.windows([11*60,16*60],[19*60,21*60],0.35)

P3_UHI_TV = P3_UHI.Appliance(P3_UHI,1,120,2,480,0.1,30)
P3_UHI_TV.windows([12*60,17*60],[19*60,24*60],0.35)

P3_UHI_Phone_charger = P3_UHI.Appliance(P3_UHI,4,5,3,180,0.2,20)
P3_UHI_Phone_charger.windows([6*60+30,7*60+30],[14*60,16*60],0.35,[18*60,20*60])

P3_UHI_Rice_Cooker = P3_UHI.Appliance(P3_UHI,1,80,2,180,0.2,30)
P3_UHI_Rice_Cooker.windows([12*60,14*60],[19*60,21*60],0.35)

P3_UHI_Fridge = P3_UHI.Appliance(P3_UHI,1,200,1,1440,0,30, 'yes',3)
P3_UHI_Fridge.windows([0,1440],[0,0])
P3_UHI_Fridge.specific_cycle_1(200,20,5,10)
P3_UHI_Fridge.specific_cycle_2(200,15,5,15)
P3_UHI_Fridge.specific_cycle_3(200,10,5,20)
P3_UHI_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

P3_UHI_laptop_wd = P3_UHI.Appliance(P3_UHI,2,120,1,120,0.2,120,wd_we_type = 0)
P3_UHI_laptop_wd.windows([18*60,22*60],[0,0],0.35)

P3_UHI_laptop_we = P3_UHI.Appliance(P3_UHI,2,120,3,240,0.2,120,wd_we_type = 1)
P3_UHI_laptop_we.windows([10*60,12*60+30],[14*60,15*60+30],0.35,[18*60,20*60])

P3_UHI_Hand_Mixer = P3_UHI.Appliance(P3_UHI,1,300,2,5,0.1,30,occasional_use = 0.5)
P3_UHI_Hand_Mixer.windows([12*60,13*60],[19*60,20*60],0.35)

P3_UHI_Iron = P3_UHI.Appliance(P3_UHI,1,300,2,60,0.2,15,occasional_use = 0.2)
P3_UHI_Iron.windows([10*60,11*60],[15*60,17*60],0.35)

P3_UHI_Toaster = P3_UHI.Appliance(P3_UHI,1,1000,1,5,0.2,5,occasional_use = 0.5)
P3_UHI_Toaster.windows([8*60,8*60+30],[0,0],0.1)

P3_UHI_Washing_machine = P3_UHI.Appliance(P3_UHI,1,500,2,180,0.1,30,occasional_use = 0.50)
P3_UHI_Washing_machine.windows([8*60,12*60],[16*60,19*60],0.2)

P3_UHI_Air_Conditioner = P3_UHI.Appliance(P3_UHI,1,500,3,300,0.2,15,occasional_use=1)
P3_UHI_Air_Conditioner.windows([22*60+30,24*60],[0,60],0.35,[13*60,15*60])

P3_UHI_Microwave= P3_UHI.Appliance(P3_UHI,1,1000,3,10,0.2,5,thermal_P_var=0.3,occasional_use = 0.33)
P3_UHI_Microwave.windows([8*60,9*60],[11*60,13*60],0.35,[20*60,21*60])
#
P3_UHI_Water_Pump= P3_UHI.Appliance(P3_UHI,1,450,2,180,0.2,180,occasional_use = 0.33)
P3_UHI_Water_Pump.windows([8*60,12*60],[16*60,19*60],0.35)

#Prototype 4 : Urban middle income households
P4_UMI_lamp = P4_UMI.Appliance(P4_UMI,6,15,2,360,0.2,10,wd_we_type = 2)
P4_UMI_lamp.windows([6*60,7*60],[18*60,24*60],0.35)

P4_UMI_fan = P4_UMI.Appliance(P4_UMI,2,75,3,240,0.2,15)
P4_UMI_fan.windows([11*60+30,15*60],[20*60,24*60],0.35,[0,6*60+30])

P4_UMI_TV = P4_UMI.Appliance(P4_UMI,1,120,2,480,0.1,30)
P4_UMI_TV.windows([12*60,17*60],[19*60,24*60],0.35)

P4_UMI_Phone_charger = P4_UMI.Appliance(P4_UMI,4,5,3,180,0.4,30)
P4_UMI_Phone_charger.windows([6*60+30,7*60+30],[14*60,16*60],0.35,[18*60,20*60])

P4_UMI_Rice_Cooker = P4_UMI.Appliance(P4_UMI,1,80,2,180,0.2,30)
P4_UMI_Rice_Cooker.windows([12*60,14*60],[19*60,21*60],0.35)

P4_UMI_Fridge = P4_UMI.Appliance(P4_UMI,1,200,1,1440,0,30, 'yes',3)
P4_UMI_Fridge.windows([0,1440],[0,0])
P4_UMI_Fridge.specific_cycle_1(200,20,5,10)
P4_UMI_Fridge.specific_cycle_2(200,15,5,15)
P4_UMI_Fridge.specific_cycle_3(200,10,5,20)
P4_UMI_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

P4_UMI_laptop_wd = P4_UMI.Appliance(P4_UMI,2,120,1,120,0.2,120,wd_we_type = 0)
P4_UMI_laptop_wd.windows([18*60,22*60],[0,0],0.35)

P4_UMI_laptop_we = P4_UMI.Appliance(P4_UMI,2,120,3,240,0.2,120,wd_we_type = 1)
P4_UMI_laptop_we.windows([10*60,12*60+30],[14*60,15*60+30],0.35,[18*60,20*60])

P4_UMI_Hand_Mixer = P4_UMI.Appliance(P4_UMI,1,300,2,5,0.1,3,occasional_use = 0.5)
P4_UMI_Hand_Mixer.windows([12*60,13*60],[19*60,20*60],0.35)

P4_UMI_Iron = P4_UMI.Appliance(P4_UMI,1,300,2,60,0.2,15,occasional_use = 0.1)
P4_UMI_Iron.windows([10*60,11*60],[15*60,17*60],0.35)

P4_UMI_Toaster = P4_UMI.Appliance(P4_UMI,1,1000,1,5,0.2,5,occasional_use = 0.5)
P4_UMI_Toaster.windows([8*60,8*60+30],[0,0],0.35)

P4_UMI_Washing_machine = P4_UMI.Appliance(P4_UMI,1,500,2,180,0.1,30,occasional_use = 0.50)
P4_UMI_Washing_machine.windows([8*60,12*60],[16*60,19*60],0.35)
#
#Prototype 5: Urban residential + commercial mixed households
P5_UMIX_lamp1 = P5_UMIX.Appliance(P5_UMIX,6,15,2,360,0.2,10,wd_we_type = 2)
P5_UMIX_lamp1.windows([5*60,7*60],[18*60,24*60],0.35)

P5_UMIX_lamp2 = P5_UMIX.Appliance(P5_UMIX,10,30,1,360,0.2,10,wd_we_type = 0)
P5_UMIX_lamp2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_fan1 = P5_UMIX.Appliance(P5_UMIX,2,75,2,240,0.2,15)
P5_UMIX_fan1.windows([11*60,16*60],[19*60,21*60],0.35)

P5_UMIX_fan2 = P5_UMIX.Appliance(P5_UMIX,4,75,1,480,0.2,15,wd_we_type = 0)
P5_UMIX_fan2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_TV1 = P5_UMIX.Appliance(P5_UMIX,1,120,2,480,0.1,30)
P5_UMIX_TV1.windows([12*60,17*60],[19*60,24*60],0.35)

P5_UMIX_TV2 = P5_UMIX.Appliance(P5_UMIX,1,120,1,300,0.1,30,wd_we_type = 0)
P5_UMIX_TV2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_Phone_charger1 = P5_UMIX.Appliance(P5_UMIX,4,5,3,180,0.1,60)
P5_UMIX_Phone_charger1.windows([6*60+30,7*60+30],[14*60,16*60],0.35,[18*60,20*60])

P5_UMIX_Phone_charger2 = P5_UMIX.Appliance(P5_UMIX,10,5,1,300,0.1,60)
P5_UMIX_Phone_charger2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_Rice_Cooker = P5_UMIX.Appliance(P5_UMIX,1,80,2,180,0.2,30)
P5_UMIX_Rice_Cooker.windows([12*60,14*60],[19*60,21*60],0.35)

P5_UMIX_Fridge = P5_UMIX.Appliance(P5_UMIX,3,200,1,1440,0,30, 'yes',3)
P5_UMIX_Fridge.windows([0,1440],[0,0])
P5_UMIX_Fridge.specific_cycle_1(200,20,5,10)
P5_UMIX_Fridge.specific_cycle_2(200,15,5,15)
P5_UMIX_Fridge.specific_cycle_3(200,10,5,20)
P5_UMIX_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

P5_UMIX_laptop_wd = P5_UMIX.Appliance(P5_UMIX,2,120,1,120,0.2,120,wd_we_type = 0)
P5_UMIX_laptop_wd.windows([18*60,22*60],[0,0],0.35)

P5_UMIX_laptop_we = P5_UMIX.Appliance(P5_UMIX,2,120,3,240,0.2,120,wd_we_type = 1)
P5_UMIX_laptop_we.windows([10*60,12*60+30],[14*60,15*60+30],0.35,[18*60,20*60])

P5_UMIX_laptop2 = P5_UMIX.Appliance(P5_UMIX,5,65,1,480,0.2,120,wd_we_type = 0)
P5_UMIX_laptop2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_computer = P5_UMIX.Appliance(P5_UMIX,5,150,1,480,0.2,60,wd_we_type = 0)
P5_UMIX_computer.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_Hand_Mixer = P5_UMIX.Appliance(P5_UMIX,1,300,2,5,0.1,2,occasional_use = 0.5)
P5_UMIX_Hand_Mixer.windows([12*60,13*60],[19*60,20*60],0.35)

P5_UMIX_Iron = P5_UMIX.Appliance(P5_UMIX,1,300,2,60,0.2,15,occasional_use = 0.1)
P5_UMIX_Iron.windows([10*60,11*60],[15*60,16*60],0.35)

P5_UMIX_Toaster = P5_UMIX.Appliance(P5_UMIX,1,1000,1,5,0.2,5,occasional_use = 0.5)
P5_UMIX_Toaster.windows([8*60+30,9*60],[0,0],0.35)

P5_UMIX_Washing_machine = P5_UMIX.Appliance(P5_UMIX,1,500,2,180,0.1,30,occasional_use = 0.50)
P5_UMIX_Washing_machine.windows([8*60,12*60],[16*60,19*60],0.35)

P5_UMIX_Air_Conditioner1 = P5_UMIX.Appliance(P5_UMIX,1,500,3,300,0.2,15,occasional_use=1)
P5_UMIX_Air_Conditioner1.windows([22*60+30,24*60],[0,60],0.35,[13*60,15*60])

P5_UMIX_Air_Conditioner2 = P5_UMIX.Appliance(P5_UMIX,4,500,1,300,0.2,15)
P5_UMIX_Air_Conditioner2.windows([9*60,19*60],[0,0],0.1)

P5_UMIX_Microwave= P5_UMIX.Appliance(P5_UMIX,1,1000,3,10,0.2,5,thermal_P_var=0.3,occasional_use = 0.33)
P5_UMIX_Microwave.windows([8*60,9*60],[11*60,13*60],0.1,[20*60,21*60])

P5_UMIX_Water_Pump= P5_UMIX.Appliance(P5_UMIX,1,450,2,180,0.2,180,thermal_P_var=0.3,occasional_use = 0.33)
P5_UMIX_Water_Pump.windows([8*60,12*60],[16*60,19*60],0.1)

P5_UMIX_others = P5_UMIX.Appliance(P5_UMIX,2,1000,1,480,0.2,30,wd_we_type = 0)
P5_UMIX_others.windows([9*60,19*60],[0,0],0.1)






