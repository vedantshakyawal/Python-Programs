#import another_module
#print(another_module.another_variable)
#
#from turtle import Turtle, Screen
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)
#
#my_screen = Screen()
#print(my_screen.canheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Spuirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l"

print(table)