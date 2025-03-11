import pyvisa

##The following two lines will need to be edited 
rm = pyvisa.ResourceManager()
P_sup = rm.open_source('name of o POWERSUPPLY string')


def powersupply (Voltage, Amp, channel):

    P_sup = rm.open_source('name of o POWERSUPPLY string')
    if channel == 1:
            CH =  'CH1'
    elif channel == 2:
            CH =  'CH2'
    else:
            CH =  'CH3'
    P_sup.write("APPL CH, Voltage, Amp ")


    return 



