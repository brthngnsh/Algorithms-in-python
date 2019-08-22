#an expression say (3+4)*2 is in RPN format if it is of the form "3,4,+2,*,"

def rpn_evaluate(rpn_expression) :
    intermediate_result = []
    delimiter = ","
    operator = {'+' : lambda x, y : x + y , '-' : lambda x , y : x - y , '*' : lambda x , y : x * y , '/' : lambda x , y: x / y}
    for token in rpn_expression.split(delimiter) :
        if token in operator :
            intermediate_result.append(operator[token](intermediate_result.pop(),intermediate_result.pop()))
        else :
            intermediate_result.append(token)
    return intermediate_result[-1]

#rpn_expression is a stack

#brthngnsh