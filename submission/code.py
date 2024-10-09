import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def set_color(color):
    for i in range(10):
        cp.pixels[i] = color
    cp.pixels.show()

while True:
    
    print("Choose a choice:")
    print("1 for Red Color")
    print("2 for Green Color")
    print("3 for Blue Color")
    print("Press 'q' to quit")

  
    preference= input("Enter your choice: ")

    if preference.lower() == 'q':
        print("Exiting the program.")
        break


    try:
        option = int(preference)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3, or 'q' to quit.")
        continue

   
    if option ==1:
        set_color((255,0,0)) 
    elif option ==2:
        set_color((0, 255, 0))  
    elif option == 3:
        set_color((0, 0, 255))
    else: 
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    
time.sleep(0.7)