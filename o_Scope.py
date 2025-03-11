import pyvisa

rm = pyvisa.ResourceManager()
O_scope = rm.open_source('name of o scope string')
O_scope.write("*CLS") #Clears current status
O_scope.write("RST")  #resets to default setup 
O_scope.write(":AUToscale:AMODE NORMal") #Sets Data aquisition time to Real-time
O_scope.write(":FUNCtion:SOURce CHANnel1")  #gets the FFT of channel 1 


O_scope.write(":TRIGger:EDGE:SOURCe CHANnel1")  #make channel 1 the edge triggered channel
O_scope.write(":TRIGger:EDGE:LEVel 1.5")  # channel is triggered at 1.5 = 0.75*full-scale value, 
