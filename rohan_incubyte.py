#!/usr/bin/env python
# coding: utf-8

# In[1]:


class GSLV:
    def __init__(self, initial_pos, initial_dir):
        self.position = initial_pos
        self.direction = initial_dir
## (x,y,z)=(self.position[0],self.position[1],self.position[2])
##initial dirc=North(Up)
    def move_forward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
            
    def move_backward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
##North->90degree left=West
##West->90degree left=South
##South->90degree left=East
##East->90degree left=North
##Up->90degree left=North
##Down->90degree left=South
    def turn_left(self):
        directions = {"N": "W", "W": "S", "S": "E", "E": "N", "Up": "N", "Down": "S"}
        self.direction = directions[self.direction]
##North->90degree right=East
##East->90degree right=South
##South->90degree right=West
##West->90degree right=North
##Up->90degree left=South
##Down->90degree left=North 
    def turn_right(self):
        directions = {"N": "E", "E": "S", "S": "W", "W": "N", "Up": "S", "Down": "N"}
        self.direction = directions[self.direction]
        
    def turn_up(self):
        if self.direction == "N" or self.direction == "S" or self.direction == "E" or self.direction == "W":
            self.direction = "Up"
            
    def turn_down(self):
        if self.direction == "N" or self.direction == "S" or self.direction == "E" or self.direction == "W":
            self.direction = "Down"

def execute_command(commands, initial_position, initial_direction):
    chandrayaan3 = GSLV(initial_position, initial_direction)

    for command in commands:
        if command == "f":
            chandrayaan3.move_forward()
        elif command == "b":
            chandrayaan3.move_backward()
        elif command == "l":
            chandrayaan3.turn_left()
        elif command == "r":
            chandrayaan3.turn_right()
        elif command == "u":
            chandrayaan3.turn_up()
        elif command == "d":
            chandrayaan3.turn_down()

    return chandrayaan3.position, chandrayaan3.direction

# Test the program
initial_pos = (0, 0, 0)
initial_dir=input("Enter initial direction (N/S/W/E):")
commands = input("Enter commands(f/r/u/b/l without spaces):")

final_position, final_direction = execute_command(commands, initial_pos, initial_dir)

print("Final Position:", final_position)
print("Final Direction:", final_direction)


# In[ ]:




