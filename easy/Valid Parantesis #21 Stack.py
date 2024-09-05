def isValid(self, s: str) -> bool:

        stack=[]
        p={
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            if char in p:  #check the key of dic
                stack.append(char)  
            elif stack and p[stack[-1]]==char:  #check if stack have somthing and value of dic is char
                stack.pop()
            else:
                return False
        return len(stack)==0