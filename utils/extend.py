def extendFunc(operand0, operand1, operator):
    switch_dict = {
        "+": [rec + operand1[idx] for idx, rec in enumerate(operand0)],
        "-": [rec - operand1[idx] for idx, rec in enumerate(operand0)],
        "*": [rec * operand1[idx] for idx, rec in enumerate(operand0)],
        "/": [rec / operand1[idx] for idx, rec in enumerate(operand0)]
    }
    return switch_dict[operator]