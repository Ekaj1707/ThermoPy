import CoolProp.CoolProp as CP  # need to install module beforehand, something like pip install CoolProp

zeroC = 273.15  #conversion value C to K. CoolProp works in SI units which are K for T

print("Input Upper Temperature in degrees Celsius: ")
upper_temp = float(input()) # adjusted to make variable T
print("Input Lower Temperature in degrees Celsius, identical for a pump: ")
lower_temp = float(input())
print("Input Mass Flow Rate in kilograms/second: ")
mdot = float(input()) # adjusted to make variable m

print("Input lower pressure in kPa")
pin = (float(input()))*1000
print("Input upper pressure in kPa")
pout = (float(input()))*1000
hin = CP.PropsSI('H','P', pin,"T",lower_temp+zeroC,'water')
hout = CP.PropsSI('H','P', pout,"T",upper_temp+zeroC,'water')

device = input("Is the device a pump/compressor or a turbine: ")


Work_pump = abs(mdot*(hout-hin))
Work_turbine = abs(mdot*(hin-hout))

if device == "pump" or device == "compressor":
    print("Pump/compressor work rate =  ",Work_pump/1000," kW")  # significant figures should be addressed
elif device == "turbine":
    print("Turbine work rate = ",Work_turbine/1000," kW")
else:
   print("Device invalid, input in lower case")
   