import pyvisa

##The following two lines will need to be edited 
rm = pyvisa.ResourceManager()
P_sup = rm.open_source('name of o POWERSUPPLY string')

#Function will be used to set the Voltage and amps of a specific channel
#CH1 max voltage = 6.18 V, Min = 0 V, Max Amp = 5.15 A, Min Amp = 0.002 A
#CH2/3 max voltage = 30.9 V, Min = 0 V, Max Amp = 1.03 A, Min Amp = 0.001 A
def Ch_Set_Vol_Amp (Voltage, Amp, channel):
        
        P_sup = rm.open_source('name of o POWERSUPPLY string')
        if channel == 1:
                CH =  'CH1'
        elif channel == 2:
                CH =  'CH2'
        else:
                CH =  'CH3'
        A = str(Amp)
        V = str(Voltage)
        Command = "APPL "+CH+", "+V+", "+A
        return P_sup.write(Command)

def Rest_P_Sup(): 
        


        return


