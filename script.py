def my_function():
    print("hello")
    print("bye")

my_function()

def turn_right():
    left_turn()
    left_turn()
    left_turn()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()