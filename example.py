def solution(s: str) -> bool :
    stack = []
    table = {
        ')' : '(' ,
        '}' : '{' ,
        ']' : '['
    }
    for char in s:
        if char not in stack:
            stack.append(char)
        elif not stack and table[char] != (q:=stack.pop()):
            print(stack)
            return False
    return len(stack) == 0


s = "(123))"
a = solution(s)
print(a)