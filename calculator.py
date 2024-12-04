#Taking input from user.
input_1=input()
length_of_input_1=len(input_1)

list_of_operators=["+","-","*","/","(",")"]
#List that contains the values
values_list=[]
#List that contains the operators
operators_in_input=[]
#Stack
input_stack=[]

#Function to convert strings to float
def list_to_number(value):
    value_string=""
    for i in value:
        value_string=value_string+i
    return float(value_string)
    
#This function seprates the numericals and the operators from the list.
def splitting_values_and_operators(openBrace,closedBrace):
    start_index=openBrace
    for i in range(openBrace,closedBrace):
        #Checking if the item is an operator 
        if input_stack[i] in list_of_operators:
            #if it is a operator append it to the operators list
            operators_in_input.append(input_stack[i])
            #converting the items before the operator into float
            number=list_to_number(input_stack[start_index:i])
            #append the value into values_list
            values_list.append(number)
            start_index=i+1
    #As we append the values before the operators there will be a value left after the operator now we append that value
    if start_index!=closedBrace-1:
        number=list_to_number(input_stack[start_index:closedBrace])
    else:
        number=list_to_number(input_stack[start_index])
    values_list.append(number)
    
#This function performs the operations on the values by following the precedence.
def calculator(start,end,length_of_operators_list):
    for i in range(length_of_operators_list):
        if "/" in operators_in_input[start:end]:
            index=operators_in_input.index('/')
            values_list[index]=values_list[index]/values_list[index+1]
            del values_list[index+1]
            del operators_in_input[index]
        elif "*" in operators_in_input[start:end]:
            index=operators_in_input.index('*')
            values_list[index]=values_list[index]*values_list[index+1]
            del values_list[index+1]
            del operators_in_input[index]
        elif "+" in operators_in_input[start:end]:
            index=operators_in_input.index('+')
            values_list[index]=values_list[index]+values_list[index+1]
            del values_list[index+1]
            del operators_in_input[index]
        elif "-" in operators_in_input[start:end]:
            index=operators_in_input.index('-')
            values_list[index]=values_list[index]-values_list[index+1]
            del values_list[index+1]
            del operators_in_input[index]
    return values_list[0]

#This is the main function that seperates all the tasks and performs the operations.
def seperator():
    openBrace=0
    closedBrace=length_of_input_1
    
    for i in range(length_of_input_1):
        #if the value is ")" as it has the highest order start performing the operationsbetween the parenthesis.
        if input_1[i]==")":
            closedBrace=len(input_stack)
            #Finding the last occurence of "("
            try:
                joined_string = ''.join(input_stack)
                openBrace = joined_string.rindex('(') + 1
            except (ValueError,TypeError) as e:
                print(f"Error: Parentheses mismatch in the input expression:{e}")
                raise
            
            splitting_values_and_operators(openBrace,closedBrace)
            length_of_operators_list=len(operators_in_input)
            #For checking print both the values_list & operators_in_input
            print(values_list)
            print(operators_in_input)
            #sub_result is the result of the operation performed in between the parenthesis
            sub_result=calculator(0,length_of_operators_list,length_of_operators_list)
            for j in range(openBrace,closedBrace+1):
                #Now remove the values from the stack
                input_stack.pop()
            #append the sub_result into the stack
            input_stack.append(str(sub_result))
            #Empty the values_list for further operations if only it isn't the final result.
            if i!=length_of_input_1-1:
                values_list.pop()
                
        else:
            #append the values into stack until it is ")"
            input_stack.append(input_1[i])
            
seperator()

print(f"The result is :{values_list[0]}")