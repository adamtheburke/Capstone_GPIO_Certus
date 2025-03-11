import pyvisa

##These will need to be edited fot the rest of the Program to work. 
rm = pyvisa.ResourceManager()
P_sup = rm.open_source('name of o POWERSUPPLY string')


def powersupply (Voltage, Amp, channel):

    Output = P_sup = rm.open_source('name of o POWERSUPPLY string')
    if channel == 1:
            CH =  'CH1'
    elif channel == 2:
            CH =  'CH2'
    else:
            CH =  'CH3'
    Output.write("APPL CH, Voltage, Amp ")


    return Output
