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



def generate_variable_values():
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
    #the canvas.mainloop function wasn't working properly when in the main function, so I wasn't able to create multiple functions like normal and made my flow a bit different than normal
    




    
    # Start the event loop to display the canvas
    

# Call the function to display the canvas
generate_variable_values()


    

