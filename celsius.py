## Jennefer Maldonado ##
## Date Due: October 16, 2020 ##
import sys

def parse_command_line(rawinput):
    #parse_command_line takes the commandline
    #arguments of sys.argv.
    #It returns useful errors.
    #This command is executed from the commandline.
    rawinput_list = ''
    #if there is more than one value eg ( 37 89 27)
    if len(rawinput) > 2:
      for r in range(1,len(rawinput)):
        rawinput_list = rawinput_list + rawinput[r] + ' '
    else: #only one thing was entered eg( 86 or 'cat')
        rawinput = str(rawinput[1])
    modified_input = ''
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for c in rawinput:
        if c in numbers: # numeric value entered it's good!
         modified_input = modified_input + c
        elif c == '-' and modified_input == '': # if a negative sign it's good!
         modified_input = modified_input + c
        else: #non numeric value we don't want
         break
    fahren = 0 #set the number to zero
    if modified_input == '': #if nothing was parsed -- give a default of 0
        print('Invalid Input: default fahrenheit value will be 0')
    else: # we have a number parsed and read to convert
        fahren = int(modified_input)
    return fahren #return it here
    #raise NotImplementedError

def calculate_celsius(degree_fahrenheit):
    #Print conversion after parse.
    # Formula for fahrenheit to celsius
    df = (degree_fahrenheit-32)*(5.0/9.0) #calculate!
    print(str(degree_fahrenheit) + "F is " + str(df) + "C") #format and print
    #raise NotImplementedError

if __name__ == "__main__":
    command_line_inputs = sys.argv
    user_fahrenheit = parse_command_line(command_line_inputs)
    calculate_celsius(user_fahrenheit)