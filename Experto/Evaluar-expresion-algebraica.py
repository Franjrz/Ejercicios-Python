import re
import operator

class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []
        
def analisis_lexico(string):
    mappings = {'+': 1, '-': 2, '*': 3, '/': 4, '(': 5, ')': 6}

    tokens = []
    buffer = ""
    for char in string:
        if char in mappings:
            if len(buffer) > 0:
                tokens.append(Node(0, value=float(buffer)))
            tokens.append(Node(mappings[char], value=char))
            buffer = ""
        else:
            buffer += char
    if len(buffer) > 0:
        tokens.append(Node(0, value=float(buffer)))
    tokens.append(Node(7))
    
    return tokens

def parse_e(tokens):
    #print("En e")
    #print(tokens[0].token_type)
    left_node = parse_ee(tokens)

    while tokens[0].token_type in [1, 2]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_ee(tokens))
        left_node = node

    return left_node

def parse_ee(tokens):
    #print("En ee")
    #print(tokens[0].token_type)
    left_node = parse_eee(tokens)

    while tokens[0].token_type in [3,4]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_eee(tokens))
        left_node = node

    return left_node

def parse_eee(tokens):
    #print("En eee")
    #print(tokens[0].token_type)
    #print(len(tokens))
    if tokens[0].token_type == 0:
        return tokens.pop(0)
    
    if tokens[0].token_type == 5:
        tokens.pop(0)
    expression = parse_e(tokens)
    if tokens[0].token_type == 6:
        tokens.pop(0)

    return expression

def parse(inputstring):
    tokens = analisis_lexico(inputstring)
    ast = parse_e(tokens)
    if tokens[0].token_type == 7:
        tokens.pop(0)
    return ast

op = {1: operator.add, 2: operator.sub, 3: operator.mul, 4: operator.truediv}

def compute(node):
    if node.token_type == 0:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = op[node.token_type]
    return operation(left_result, right_result)

def calc(expression):
    expression = re.sub(r'\s*\-\s*\-\s*', '+',   expression)
    expression = re.sub(r'\s*\+\s*\-\s*', '-',   expression)
    expression = re.sub(r'\s+', '',   expression)
    if expression[0] == '-':
        expression = '0'+expression
    expression = re.sub(r'\(\-', '(0-',   expression)
    expression = re.sub(r'\*\-', '*(0-1)*',   expression)
    expression = re.sub(r'\/\-', '*(0-1)/',   expression)
    return(compute(parse(expression)))