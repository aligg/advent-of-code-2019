inp = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,31,68,225,1001,13,87,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,174,110,224,1001,224,-46,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,13,60,224,101,-73,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,87,72,225,101,47,84,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,76,31,225,1102,60,43,225,1102,45,31,225,1102,63,9,225,2,170,122,224,1001,224,-486,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,29,17,224,101,-493,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,52,54,225,1102,27,15,225,102,26,113,224,1001,224,-1560,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1002,117,81,224,101,-3645,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226]

test_input = [3,9,8,9,10,9,4,9,99,-1,8]

OPCODE1 = 1
OPCODE2 = 2
OPCODE3 = 3
OPCODE4 = 4
OPCODE5 = 5
OPCODE6 = 6
OPCODE7 = 7
OPCODE8 = 8
PARAM_MODE_0 = 0 # parameter is interpreted as a position
PARAM_MODE_1 = 1 # parameter is interpreted as a value

def determine_mode(number):
    number = f"{number:05}" # add zeroes
    first_parameter_mode = int(number[2])
    second_parameter_mode = int(number[1])
    third_parameter_mode = int(number[0])
    opcode = int(number[3:])
    return [first_parameter_mode, second_parameter_mode, third_parameter_mode, opcode]

def do_computing(inp):
    INP = inp
    i = 0
    while INP[i] != 99:
        first_param_mode, second_param_mode, third_param_mode, opcode = determine_mode(INP[i])
        if opcode in [OPCODE1, OPCODE2, OPCODE7, OPCODE8]:
            handle_operation()
        elif opcode == OPCODE3:
            user_input = int(input('enter input: ')) # solicit user input
            INP[INP[i+1]] = user_input # stores that input at index of i+1
            i += 2
        elif opcode == OPCODE4:
            # return value at index specified at following index
            print(INP[INP[i+1]])
            i += 2
        elif opcode == OPCODE5:
            pass
        elif opcode == OPCODE6:
            pass
        return
    return INP

# def do_computing(inp):
#         INP = inp
#         count = 0
#         i = 0
#         while i < len(INP):
#             if i != count:
#                 i+=1
#                 continue
            
#             positions = mode_arr(INP[i])
#             position_one_mode = positions[2]
#             position_two_mode = positions[1]

          
#             val_three = INP[i+3]

#             print("INDEX", i)
#             print("VALUE", INP[i])
#             print("INP", INP)
#             if INP[i] % 100 == OPCODE1:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 # add values stored at indices i+1 and i+2
#                 sum = val_one + val_two
#                 # assign sum to index of value stored at i+3
#                 INP[val_three] = sum
#                 # skip forward
#                 count += 4
#             elif INP[i]  % 100== OPCODE2:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 # multiply values stored at indices i+1 and i+2
#                 product = val_one * val_two
#                 # assign sum to index of value stored at i+3
#                 INP[val_three] = product
#                 # skip forward
#                 count += 4
#             elif INP[i]  % 100== OPCODE3:
#                 # takes a single integer as input
#                 user_input = int(input('enter input: '))
#                 INP[INP[i+1]] = user_input
#                 # stores that input at index of i+1
#                 count += 2
#             elif INP[i]  % 100 == OPCODE4:
#                 # return value at index specified at following index
#                 print(INP[INP[i+1]])
#                 count += 2
#             elif INP[i] % 100 == OPCODE5:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 # if first param is non-zero
#                 # set instruction pointer to the value from second parameter
#                 if val_one != 0:
#                     i = val_two
#                     continue
#                 count +=3
#             elif INP[i] % 100 == OPCODE6:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 if val_one == 0:
#                     i = val_two
#                     continue
#                 count += 4
#             elif INP[i] % 100 == OPCODE7:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 if val_one < val_two:
#                     INP[INP[i+3]] == 1
#                 else:
#                     INP[INP[i+3]] == 0
#                 count += 4
#             elif INP[i] % 100 == OPCODE8:
#                 if position_one_mode == PARAM_MODE_0:
#                     val_one = INP[INP[i + 1]]
#                 else:
#                     val_one = INP[i + 1]
#                 if position_two_mode == PARAM_MODE_0:
#                     val_two = INP[INP[i +2]] if INP[i+2] in INP else 0
#                 else: 
#                     val_two = INP[i + 2]
#                 if val_one == val_two:
#                     INP[INP[i+3]] == 1
#                 else:
#                     INP[INP[i+3]] == 0
#                 count +=4
#             elif INP[i]  % 100 == 99:
#                 print(INP)
#                 return INP
#             else:
#                 print("PROBLEM")
#                 print("INDEX", i)
#                 print("VALUE", INP[i])
#                 print("INP", INP)
#                 return INP
#             i += 1
    

if __name__ == "__main__":
    do_computing(test_input)
    # mode_map(3)


# borrowed code from ali spittel so I could move on

def get_modes(modes):
    # print(modes)
    return [int(mode) for mode in [modes[2], modes[1], modes[0], modes[3:]]]


def get_param(mode, increment, idx, data):
    if mode == 0:
        return data[data[idx + increment]]
    return data[idx + increment]

def get_params(mode1, mode2, idx, data):
    return get_param(mode1, 1, idx, data), get_param(mode2, 2, idx, data)


def call_operation(mode1, mode2, idx, data, operation):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return operation(param1, param2), idx + 4

def add(param1, param2):
    return param1 + param2

def multiply(param1, param2):
    return param1 * param2

def less_than(param1, param2):
    return 1 if param1 < param2 else 0

def equals(param1, param2):
    return 1 if param1 == param2 else 0

def jump_if_true(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 != 0 else idx + 3

def jump_if_false(mode1, mode2, idx, data):
    param1, param2 = get_params(mode1, mode2, idx, data)
    return param2 if param1 == 0 else idx + 3


def calculate(data, input_val):
    idx = 0
    diagnostic_code = None
    while data[idx] != 99:
        mode1, mode2, _, opcode = get_modes(f"{data[idx]:05}")
        OPERATIONS = {1: add, 2: multiply, 7: less_than, 8: equals}
        if opcode in OPERATIONS:
            data[data[idx + 3]], idx = call_operation(
                mode1, mode2, idx, data, OPERATIONS[opcode]
            )
        elif opcode == 3:
            data[data[idx + 1]] = input_val
            idx += 2
        elif opcode == 4:
            diagnostic_code = data[data[idx + 1]]
            idx += 2
        elif opcode == 5:
            idx = jump_if_true(mode1, mode2, idx, data)
        elif opcode == 6:
            idx = jump_if_false(mode1, mode2, idx, data)
    return diagnostic_code


# with open("input.txt") as _file:
#     for line in _file:
#         input_vals = [int(num) for num in line.split(",")]
#         print(f"Part 1: {calculate(input_vals[:], 1)}")
#         print(f"Part 2: {calculate(input_vals[:], 5)}")

# if __name__ == "__main__":
    # do_computing(test_input)
    # mode_map(3)
    # print(calculate(inp[:], 5))
    # print(f"Part 2: {calculate(inp[:], 5)}")()
