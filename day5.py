
OPCODE1 = 1
OPCODE2 = 2
OPCODE3 = 3
OPCODE4 = 4

PARAM_MODE_0 = 0
PARAM_MODE_1 = 1


def do_computing(input, mode):
    # parameter is interpreted as a position
    if mode == PARAM_MODE_0:
        INP = input
        count = 0
        for i in range(len(INP)):
            if i != count:
                continue
            elif INP[i] == OPCODE1:
                # add values stored at indices i+1 and i+2
                sum = INP[INP[i + 1]] + INP[INP[i+2]]
                # assign sum to index of value stored at i+3
                INP[INP[i+3]] = sum
                # skip forward
                count += 4
            elif INP[i] == OPCODE2:
                # multiply values stored at indices i+1 and i+2
                product = INP[INP[i + 1]] * INP[INP[i+2]]
                # assign sum to index of value stored at i+3
                INP[INP[i+3]] = product
                # skip forward
                count += 4
            elif INP[i] == OPCODE3:
                # takes a single integer as input
                # stores that input at index of i+1
                pass
            elif INP[i] == OPCODE4:
                # return value at index specified at following index
                return INP[INP[i+1]]
            elif INP[i] == 99:
                # print(INP)
                return INP
            else:
                print("PROBLEM")
                return INP
    # parameter is interpreted as a value
    elif mode == 1:
        # opcode is 1s and 10s place (rightmost)
        pass

    # 1002 => 2 means multiplication


if __name__ == "__main__":
    do_computing()
