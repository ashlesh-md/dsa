# Correct Solution

def isValid(string):
    brackets = {
        '(': ')' ,
        '{' : '}' ,
        '[' : ']'
    }
    stack = []
    if len(string) <= 1:
        return "False"
    for char in string:
        if char in brackets.keys():
            stack.append(char)
        else:
            if stack:
                if brackets.get(stack.pop(len(stack) - 1)) != char:
                    return 'false'
            else:
                return 'false'
    return "False" if stack else "True"
print(isValid("(]"))
print(isValid("()"))
print(isValid("({})"))
print(isValid("({}])"))
print(isValid("[{(({}])}]"))
