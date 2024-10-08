# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:14 2024

@author: ahernandez
"""

#Well Current conditions 
Liquid_Rates = 2000     #BLPD 

Oil_Rates = 1400        #BOPD 

Water_Cut = (Liquid_Rates - Oil_Rates)/Liquid_Rates    #%

Pwf = 1100              #psi 

Pr = 4100               #psi 

Productivity_Index = (Liquid_Rates)/(Pr - Pwf)         #bbl/d/psi

print(Water_Cut)
print(Productivity_Index)

#Well Liquid Rate Increase with Frequency Change 

Current_Frequency = 51   #hZ

New_Frequency = 53       #hZ 

Frequency_Increase = New_Frequency - Current_Frequency

Percentage_Inc_Frequency = (New_Frequency/Current_Frequency) * 100  #Percentage increase in frequency

print(Percentage_Inc_Frequency)

Frequency_Ratio = Percentage_Inc_Frequency/100

New_Liquid_Rate = Liquid_Rates * Frequency_Ratio

print(New_Liquid_Rate)

#Bottomhole Flowing Pressure Calculation 

#CASE 1: ASSUMES WATER CUT STAYS CONSTANT AND WE ONLY SEE AN INCREASE IN OIL RATES 
New_Oil_Rates_Case1 = New_Liquid_Rate * (1-Water_Cut)  #USES CURRENT WC 

New_Pwf = Pr - (New_Oil_Rates_Case1/Productivity_Index)  #psi 

print (New_Pwf)
print (New_Oil_Rates_Case1)

#CASE 2: ASSUMES WATER CUT INCREASES WITH INC FREQUENCY 

if 2<= Frequency_Increase <=5:    #assumes an increase in frequency by 5-10%
    Water_Cut_New = 0.02+Water_Cut                #assumes we increase WC 5-10%
    New_Oil_Rates_Case2 = New_Liquid_Rate * Water_Cut_New
    New_Pwf_Case2 = Pr - (New_Oil_Rates_Case2/Productivity_Index)
    
    print(New_Pwf_Case2)

elif Frequency_Increase < 2:
     Water_Cut_New = 0.005 + Water_Cut
     New_Oil_Rates_Case2 = New_Liquid_Rate * Water_Cut_New
     New_Pwf_Case2 = Pr - (New_Oil_Rates_Case2/Productivity_Index)

print(New_Pwf_Case2)
print(New_Oil_Rates_Case2)



