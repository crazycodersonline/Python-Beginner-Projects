health = 100
money = 40
time = 45

def show_param():
    global health, money , time
    print(f"Health:{health} , time:{time} , money:{money}")
    
name = input("Enter your name:")
print(f"Hello {name} welcome to our adventure game")
print(f'You have health:{health} , money:{money} , you have to reach school within {time} minutes')

travel_mode = input("Do you want to take bus or taxi?")
if travel_mode == 'taxi':
    print("You had to walk to the taxi stand, ")
    print("It took you 5 minutes and it costed you 10 health points")
    health -= 10
    time -= 5
    show_param()
    
    taxi_type = input("Do you want to take personal taxi or sharing taxi?(peronal/sharing)")
    if taxi_type == 'sharing':
        print("You have reached the school")
        print('It costed you 10 health points and 15 rupees , also it took you 25 min')
        health -= 10
        money -= 15
        time -= 25
        
    else:
        print("You have reached the school")
        print('It costed you 0 health points and 30 rupees , also it took you 20 min')
        money -= 30
        time -= 20
        

else:
    print('You had to walk upto bus stand')
    print("It took you 3 min and 5 health points")
    health -= 5
    time -= 3
    show_param()
    
    bus_type = input("Do you want to take the crowded bus or wait for another?(wait/crowded)")
    if bus_type == 'wait':
        print("YOu have reached your school")
        print("It costed you 35 min , 20 ruppes and 30 health ")
        health -= 30
        money -= 20
        time -= 35
        
    else:
        print("You have reached the school")
        print("it costed you 28 min , 20 rupees and 40 health points")
        health -= 10
        money -= 20
        time -= 28
        
        
show_param()
        