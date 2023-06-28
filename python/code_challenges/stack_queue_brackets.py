from data_structures.queue import Queue


def multi_bracket_validation(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != char:
                return False

    return len(stack) == 0
