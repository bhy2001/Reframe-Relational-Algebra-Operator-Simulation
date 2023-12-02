def extendFunc(operand0, operand1, operatetion):
    switch_dict = {
        "+": [rec + operand1[0][idx] for idx, rec in enumerate(operand0[0])],
        "-": [rec - operand1[0][idx] for idx, rec in enumerate(operand0[0])],
        "*": [rec * operand1[0][idx] for idx, rec in enumerate(operand0[0])],
        "/": [rec / operand1[0][idx] for idx, rec in enumerate(operand0[0])]
    }
    return switch_dict[operatetion]
    
    