"""
The intention for this project is to help students practice and get familar with the thermo-
dynamic processes for physics 1 as I found it to be confusing at first, but through doing 
multiple problems, I was really able to get comfortable with it. This program aims to 
create unique problems each time you run it by providing different values for variables. You are to use the ideal gas law(pressure*volume = numberofparticles*idealgasconstant*temp)
to find the missing values. You will then be able to identify what type of state changes are present.
"""

import math
import random
from graphics import Canvas

NUMBER_OF_MOLECULES = 6.314
IDEAL_GAS_CONSTANT = 0.0821
def main():
    reveiling_variable_values()
    adiabatic_or_isothermal = random.randint(0,1) # 0 for adiabatic, 1 for isothermal
    if adiabatic_or_isothermal == 0:
        generate_values_adiabatic()
    elif adiabatic_or_isothermal == 1:
        generate_values_isothermal()
    if second_state_pressure > first_state_pressure:
        correct_values = {a_pressure:first_state_pressure, 
            a_volume:first_state_volume, 
            a_temperature: first_state_pressure * first_state_volume / (NUMBER_OF_MOLECULES * IDEAL_GAS_CONSTANT),
            b_pressure:second_state_pressure,
            b_volume:second_state_volume,
            b_temperature: second_state_pressure * second_state_volume / (NUMBER_OF_MOLECULES * IDEAL_GAS_CONSTANT)}
    elif second_state_pressure < first_state_pressure:
        correct_values = {a_pressure:second_state_pressure, 
            a_volume:second_state_volume, 
            a_temperature: second_state_pressure * second_state_volume / (NUMBER_OF_MOLECULES * IDEAL_GAS_CONSTANT),
            b_pressure:first_state_pressure,
            b_volume:first_state_volume,
            b_temperature: first_state_pressure * first_state_volume / (NUMBER_OF_MOLECULES * IDEAL_GAS_CONSTANT)}
    canvas.mainloop()
    generate_c_values(correct_values)

#def generate_c_values(correct_values):
    #if correct_values[a_volume] > correct_values[b_volume]:
        


def generate_values_adiabatic():
    momotonic_or_diatomic = random.randint(0,1) # 0 for monatomic, 1 for diatomic
    if momotonic_or_diatomic == 0:
        # Monatomic gas
        specific_heat_volume = 3/2 * IDEAL_GAS_CONSTANT
        specific_heat_pressure = 5/2 * IDEAL_GAS_CONSTANT
    elif momotonic_or_diatomic == 1:
        # Diatomic gas
        specific_heat_volume = 5/2 * IDEAL_GAS_CONSTANT
        specific_heat_pressure = 7/2 * IDEAL_GAS_CONSTANT

    heat_capacity_ratio = specific_heat_pressure / specific_heat_volume

    first_state_pressure = random.randint(100000,500000)
    first_state_volume = round(random.uniform(0.001,0.999), 3)

    first_value_total = (first_state_pressure) * ((first_state_volume) ** heat_capacity_ratio)
    second_state_pressure = random.randint(100000,500000)
    second_state_volume_with_heat_capacity_ratio = first_value_total / second_state_pressure
    second_state_volume = second_state_volume_with_heat_capacity_ratio ** (1/heat_capacity_ratio)

    return first_state_pressure, first_state_volume, second_state_pressure, second_state_volume



def generate_values_isothermal():
    first_state_pressure = random.randint(100000,500000)
    first_state_volume = round(random.uniform(0.001,0.999), 3)

    second_state_pressure = random.randint(100000,500000)
    second_state_volume = (first_state_pressure * first_state_volume) / second_state_pressure

    print(f"The first state's pressure is {first_state_pressure} Pa")
    print(f"The first state's volume is {first_state_volume} m^3")
    print(f"The second state's pressure is {second_state_pressure} Pa")
    print(second_state_volume)
    return first_state_pressure, first_state_volume, second_state_pressure, second_state_volume


def reveiling_variable_values():
    values = [0,0,0,0,0,0,0,0,0]
    elem1 = random.randint(0,8)
    elem2 = random.randint(0,8)
    elem3 = random.randint(0,8)
    while elem1 == elem2 or elem1 == elem3:
        elem2 = random.randint(0,8)
        elem3 = random.randint(0,8)
    while elem2 == elem3:
        elem3 = random.randint(0,8)
    print(f"{elem1}")
    print(f"{elem2}")
    print(f"{elem3}") 
    #generating value for elem1 based off what column it is in
    if elem1 == 0 or elem1 ==3 or elem1 == 6:
        values[elem1] = random.randint(100000,500000)
    elif elem1 == 1 or elem1 == 4 or elem1 == 7:
        values[elem1] = round(random.uniform(0.001,0.999), 3)
    elif elem1 == 2 or elem1 == 5 or elem1 == 8:
        values[elem1] = random.randint(100,500)
    #generating value for elem2 based off what column it is in
    if elem2 == 0 or elem2 ==3 or elem2 == 6:
        values[elem2] = random.randint(100000,500000)
    elif elem2 == 1 or elem2 == 4 or elem2 == 7:
        values[elem2] = round(random.uniform(0.001,0.999), 3)
    elif elem2 == 2 or elem2 == 5 or elem2 == 8:
        values[elem2] = random.randint(100,500)
    #generating value for elem3 based off what column it is in
    if elem3 == 0 or elem3 ==3 or elem3 == 6:
        values[elem3] = random.randint(100000,500000)
    elif elem3 == 1 or elem3 == 4 or elem3 == 7:
        values[elem3] = round(random.uniform(0.001,0.999), 3)
    elif elem3 == 2 or elem3 == 5 or elem3 == 8:
        values[elem3] = random.randint(100,500)


    # creating the table to display the values we just generated
    canvas = Canvas(800, 600, title="Thermodynamic Processes Study")

    canvas.set_canvas_background_fill("white")
    
    y = 0
    for i in range(4):
        for i in range(4):
            rectangle = canvas.create_rectangle(50 + (i*150), 50 + (y*50), 200 + (i*150), 100 + (y*50), fill="white", outline="black")
        y += 1
    canvas.create_text(100, 70, text = "State", font = "Arial 12")
    canvas.create_text(250, 70, text = "Pressure(Pa)", font = "Arial 12")
    canvas.create_text(400, 70, text = "Volume(m^3)", font = "Arial 12")
    canvas.create_text(550, 70, text = "Temperature(K)", font = "Arial 12")
    canvas.create_text(120, 120, text = "a", font = "Arial 12")
    canvas.create_text(120, 170, text = "b", font = "Arial 12")
    canvas.create_text(120, 220, text = "c", font = "Arial 12")
   
    
    x = 0
    y = 0
    for index in range(len(values)):
        value= values[index]
        if value == 0:
            canvas.create_text(250 + (x*150), 120 + (y*50), text = "?", font = "Arial 12")
        elif value > 0:
            canvas.create_text(250 + (x*150), 120 + (y*50), text = str(value), font = "Arial 12")
        x += 1
        if index == 2 or index == 5:
            y += 1
            x = 0
    
    
    canvas.mainloop()
    #the canvas.mainloop function wasn't working properly when in the main function, so my control might look a little weird
    




    
    # Start the event loop to display the canvas
    

# Call the function to display the canvas




    

if __name__ == "__main__":
        main()