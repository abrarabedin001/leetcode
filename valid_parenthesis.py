class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackPointer = 0
        openings = ['(','[','{']

        for element in s:
          
            if element in openings:
                stack.append(element)
                stackPointer+=1
            else:
                if stackPointer==0:
                  
                    return False
                else:
                    poppedElement = stack.pop(-1)
                 
                    if poppedElement == '(' and element==')':
                        stackPointer-=1
                    elif poppedElement == '[' and element==']':
                        stackPointer-=1
                    elif poppedElement == '{' and element=='}':
                        stackPointer-=1
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
        
