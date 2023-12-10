import operator
operator_dict = {
    "=": operator.eq,
    ">": operator.gt, 
    "<": operator.lt, 
    ">=": operator.ge, 
    "<=": operator.le
}

def select_aux(db, operand1, operator, operand2):
    result = {}
    for col in db:
        result[col] = []
    if operand2 in db:
        for i in range(len(db[operand1])):
            if operator_dict[operator](db[operand1][i],db[operand2][i]):
                for col in db:
                    result[col].append(db[col][i])
    else:
        try:
            if int(operand2):
                for i in range(len(db[operand1])):
                    if operator_dict[operator](db[operand1][i],int(operand2)):
                        for col in db:
                            result[col].append(db[col][i])
            elif float(operand2):
                for i in range(len(db[operand1])):
                    if operator_dict[operator](db[operand1][i],float(operand2)):
                        for col in db:
                            result[col].append(db[col][i])
        except:
            for i in range(len(db[operand1])):
                    if operator_dict[operator](db[operand1][i],operand2):
                        for col in db:
                            result[col].append(db[col][i])
    return result
        