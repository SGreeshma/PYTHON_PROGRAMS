# VALID PARENTHESIS
def isValid(s):
    stack=[]
    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if(len(stack)==0):
                return False
            x=stack.pop()
            if((x=="(" and i==")") or (x=="[" and i=="]") or (x=="{" and i=="}")):
                continue
            else:
                return False
    return len(stack)==0