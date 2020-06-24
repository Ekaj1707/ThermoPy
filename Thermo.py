import CoolProp.CoolProp as CP 
zeroC = 273.15
pump_group = ["pump", "compressor", "boiler", "evaporator"]
turbine_group = ["turbine", "condenser"]
properties = ["temperature", "pressure", "entropy", "quality"]
findable = ["work rate", "heat rate", "work", "heat", "isentropic efficiency", "second law efficiency", "carnot efficiency"]
fluid = input("What is the working fluid: ").casefold()
while fluid != "water" and fluid != "r-134a" and fluid != "r134a" and fluid != "methane":
    print("Fluid Invalid")
    fluid = input("What is the working fluid: ").casefold()
if fluid == 'water':
    substance = "IF97::water"
elif fluid == 'r-134a' or fluid == 'r134a':
    substance = "R134a"
elif fluid == "methane":
    substance = "methane"
def find_work():
    print("Available properties are " + str(properties))
    prop_a = input("What is the first property of the initial state: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the initial state: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[2]:
        prop_1 = "S"
        val_1 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the initial state: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the initial state: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second property of the initial state: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[2]:
        prop_2 = "S"
        val_2 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    u1 = CP.PropsSI('U',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Initial internal energy is: " + str(round((u1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the final state: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the final state: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[2]:
        prop_3 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_3 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_3 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the final state: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the second property of the final state: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[2]:
        prop_4 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_4 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_4 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    u2 = CP.PropsSI('U',prop_3, val_3,prop_4,val_4, substance) 
    print("Final internal energy is: " + str(round((u2/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass of the system: "))
    Work_in = m*(u2-u1)
    Work_out = m*(u1-u2)
    device = input("Is work/heat flowing in or out: ").casefold()
    while device != "in" and device != "out":
        print("Invalid response")
        device = input("Is work/heat flowing in or out: ").casefold()
    if device == "in":
            print(round((Work_in/1000), 2), " kJ of work has been done on the system/heat has been supplied to the system")
    elif device in turbine_group:
        print(round((Work_in/1000), 2), " kJ of work has been done by the system/heat has been removed from the system")
    return Work_in, Work_out, device, u1, u2, m, prop_a, prop_b, prop_c, prop_d, units_a, units_b, units_c, units_d, val_a, val_b, val_c, val_d

def find_work_rate():
    print("Available properties are " + str(properties))
    prop_a = input("What is the first property of the inlet: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the inlet: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[2]:
        prop_1 = "S"
        val_1 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the inlet: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the inlet: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second known: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[2]:
        prop_2 = "S"
        val_2 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    h1 = CP.PropsSI('H',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Inlet enthalpy is: " + str(round((h1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the outlet: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the inlet: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[2]:
        prop_3 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_3 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_3 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the first property of the inlet: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[2]:
        prop_4 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_4 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_4 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    h2 = CP.PropsSI('H',prop_3, val_3,prop_4,val_4, substance) 
    print("Outlet enthalpy is: " + str(round((h2/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass flow rate of the system: "))
    Work_pump = m*(h2-h1)
    Work_turbine = m*(h1-h2)
    device = input("Input device name: ").casefold()
    while device not in pump_group and device not in turbine_group:
        print("Device invalid")
        device = input("Input device name: ").casefold()
    if device in pump_group:
        if device == pump_group[0]:
            print("Pump work rate =  ",round((Work_pump/1000), 2), " kW")
        elif device == pump_group[1]:
            print("Compressor work rate =  ",round((Work_pump/1000), 2), " kW")
        elif device == pump_group[2]:
            print("Boiler heat rate =  ",round((Work_pump/1000), 2), " kW")
        else:
            print("Evaporator heat rate =  ",round((Work_pump/1000), 2), " kW")
    elif device in turbine_group:
        if device == turbine_group[0]:
            print("Turbine work rate = ",round((Work_turbine/1000), 2), " kW")
        else:
            print("Condenser heat rate = ",round((Work_turbine/1000), 2), " kW")
    return Work_pump, Work_turbine, device, h1, h2, m, prop_a, prop_b, prop_c, prop_d, units_a, units_b, units_c, units_d, val_a, val_b, val_c, val_d


def find_efficiency():
    prop_a = input("What is the first property of the inlet: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the inlet: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the inlet: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the inlet: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second known: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    h1 = CP.PropsSI('H',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Inlet enthalpy is: " + str(round((h1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the outlet: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the outlet: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
           print("Quality must be between 1 and 0")
           qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    h2a = CP.PropsSI('H',prop_3, val_3,prop_4,val_4, substance)
    h2s = CP.PropsSI('H', prop_3, val_3, 'S', CP.PropsSI('S', prop_1, val_1, prop_2, val_2, substance), substance)
    print("Outlet enthalpy is: " + str(round((h2a/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass flow rate of the system: "))
    Work_turbine = m*(h1-h2a)
    Work_isen = m*(h1-h2s)
    print("Turbine work rate = ",round((Work_turbine/1000), 2), " kW")
    print("Isentropic turbine work rate = ", round((Work_isen/1000), 2), " kW")
    print("Isentropic efficiency of the Turbine = ", Work_turbine/Work_isen, "%")
    return Work_isen, Work_turbine, h1, h2a, h2s, m, prop_a, prop_b, prop_c, prop_d, units_a, units_b, units_c, units_d, val_a, val_b, val_c, val_d

def turbine():
    prop_a = input("What is the first property of the inlet: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the inlet: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the inlet: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the inlet: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second known: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    h1 = CP.PropsSI('H',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Inlet enthalpy is: " + str(round((h1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the outlet: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the outlet: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[2]:
        prop_3 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_3 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_3 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[2]:
        prop_4 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_4 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_4 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    h2a = CP.PropsSI('H',prop_3, val_3,prop_4,val_4, substance)
    print("Outlet enthalpy is: " + str(round((h2a/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass flow rate of the system: "))
    Work_turbine = m*(h1-h2a)
    print("Turbine work rate = ",round((Work_turbine/1000), 2), " kW")
    return Work_turbine

def compressor():
    prop_a = input("What is the first property of the inlet: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the inlet: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the inlet: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the inlet: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second known: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    h1 = CP.PropsSI('H',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Inlet enthalpy is: " + str(round((h1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the outlet: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the outlet: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[2]:
        prop_3 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_3 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_3 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[2]:
        prop_4 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_4 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_4 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    h2a = CP.PropsSI('H',prop_3, val_3,prop_4,val_4, substance)
    print("Outlet enthalpy is: " + str(round((h2a/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass flow rate of the system: "))
    Work_compressor = m*(h2a-h1)
    print("Compressor work rate = ",round((Work_compressor/1000), 2), " kW")
    return Work_compressor

def boiler():
    prop_a = input("What is the first property of the inlet: ").casefold()
    while prop_a not in properties:
        print("Invalid property")
        prop_a = input("What is the first property of the inlet: ").casefold()
    if prop_a == properties[0]:
        prop_1 = "T"
        val_1 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_a == properties[1]:
        prop_1 = "P"
        val_1 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_a == properties[3]:
        prop_1 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_1 = qual
    prop_b = input("What is the second property of the inlet: ").casefold()
    while prop_b not in properties:
        print("Invalid property")
        prop_b = input("What is the first property of the inlet: ").casefold()
    while prop_b == prop_a:
        print("Both knowns must be different")
        prop_b = input("What is the second known: ").casefold()
    if prop_b == properties[0]:
        prop_2 = "T"
        val_2 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_b == properties[1]:
        prop_2 = "P"
        val_2 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_b == properties[3]:
        prop_2 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_2 = qual
    h1 = CP.PropsSI('H',prop_1, val_1,prop_2,val_2, substance)
    if prop_a != properties[1]:
        if prop_a != properties[0]:
            val_a = val_1
        else:
            val_a = val_1 - zeroC
    else:
        val_a = val_1/1000
    if prop_b != properties[1]:
        if prop_b != properties[0]:
            val_b = val_2
        else:
            val_b = val_2 - zeroC
    else:
        val_b = val_2/1000
    if prop_a == properties[0]:
        units_a = " degrees C"
    elif prop_a == properties[1]:
        units_a = " kPa"
    elif prop_a == properties[2]:
        units_a = " kJ/kg*K"
    else:
        units_a = ""
    if prop_b == properties[0]:
        units_b = " degrees C"
    elif prop_b == properties[1]:
        units_b = " kPa"
    elif prop_b == properties[2]:
        units_b = " kJ/kg*K"
    else:
        units_b = ""
    print("Inlet enthalpy is: " + str(round((h1/1000), 2)) + " kilojoules per kilogram when " + str(prop_a) + " is " + str(val_a) + units_a + " and " + str(prop_b) + " is " + str(val_b) + units_b +  ".")
    prop_c = input("What is the first property of the outlet: ").casefold()
    while prop_c not in properties:
        print("Invalid property")
        prop_c = input("What is the first property of the outlet: ").casefold()
    if prop_c == properties[0]:
        prop_3 = "T"
        val_3 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_c == properties[1]:
        prop_3 = "P"
        val_3 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_c == properties[2]:
        prop_3 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_3 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_3 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_c == properties[3]:
        prop_3 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_3 = qual
    prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d not in properties:
        print("Invalid property")
        prop_d = input("What is the second property of the outlet: ").casefold()
    while prop_d == prop_c:
        print("Both knowns must be different")
        prop_d = input("What is the second known: ").casefold()
    if prop_d == properties[0]:
        prop_4 = "T"
        val_4 = float(input("Input the Temperature in degrees Celsius: ")) + zeroC
    elif prop_d == properties[1]:
        prop_4 = "P"
        val_4 = float(input("Input the Pressure in kilopascals: ")) * 1000
    elif prop_d == properties[2]:
        prop_4 = "S"
        isen = input("Is the system isentropic (Y/n): ").casefold()
        if isen == "y":
            val_4 = CP.PropsSI('S',prop_1, val_1,prop_2,val_2, substance)
        else:
            val_4 = float(input("Input the Entropy in kilojoules per kilogram kelvin: "))
    elif prop_d == properties[3]:
        prop_4 = "Q"
        qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        while qual > 1 or qual < 0:
            print("Quality must be between 1 and 0")
            qual = float(input("What is the quality of the mixture (1 for sat vapour or 0 for sat liquid): "))
        val_4 = qual
    if prop_c != properties[1]:
        if prop_c != properties[0]:
            val_c = val_3
        else:
            val_c = val_3 - zeroC
    else:
        val_c = val_3/1000
    if prop_d != properties[1]:
        if prop_d != properties[0]:
            val_d = val_4
        else:
            val_d = val_4 - zeroC
    else:
        val_d = val_4/1000
    if prop_c == properties[0]:
        units_c = " degrees C"
    elif prop_c == properties[1]:
        units_c = " kPa"
    elif prop_c == properties[2]:
        units_c = " kJ/kg*K"
    else:
        units_c = ""
    if prop_d == properties[0]:
        units_d = " degrees C"
    elif prop_d == properties[1]:
        units_d = " kPa"
    elif prop_d == properties[2]:
        units_d = " kJ/kg*K"
    else:
        units_d = ""
    h2a = CP.PropsSI('H',prop_3, val_3,prop_4,val_4, substance)
    print("Outlet enthalpy is: " + str(round((h2a/1000), 2)) + " kilojoules per kilogram when " + str(prop_c) + " is " + str(val_c) + units_c + " and " + str(prop_d) + " is " + str(val_d) + units_d + ".")
    m = float(input("What is the mass flow rate of the system: "))
    Heat_boiler = m*(h2a-h1)
    print("Boiler heat rate = ",round((Heat_boiler/1000), 2), " kW")
    return Heat_boiler

def find_carnot():
    Tmax = float(input("Input maximum environmental temperature: "))+zeroC
    Tmin = float(input("Input minimum environmental temperature: "))+zeroC
    WTurbine = turbine()
    WCompressor = compressor()
    HBoiler = boiler()
    Wnet = WTurbine-WCompressor
    Efficiency = Wnet/HBoiler
    print("The thermal efficiency of the system is ", Efficiency*100, "%")
    Carnot_Efficiency = float(1-(Tmin/Tmax))
    print("The carnot efficiency of the system is ", Carnot_Efficiency*100, "%")
    Second_Law_Efficiency = Efficiency/Carnot_Efficiency
    print("The second law efficiency of the system is ", Second_Law_Efficiency*100, "%")



what_find = input("What is being searched for " + str(findable) + ": ")
while what_find not in findable:
    print("Invalid")
    what_find = input("What is being searched for " + str(findable) + ": ")
if what_find == findable[0] or what_find == findable[1]:
    find_work_rate()
elif what_find == findable[2] or what_find == findable[3]:
    find_work()
elif what_find == findable[4]:
    find_efficiency()
elif what_find == findable[5] or what_find == findable[6]:
    find_carnot()