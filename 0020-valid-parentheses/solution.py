class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =[]
        matching ={

            ")":"(",
            "]":"[",
            "}":"{"
        } 

        for every_char in s:

            if every_char in {"(", "[", "{"}: # daca incepe paranteza, adaugam in stack
                stack.append(every_char)
            else:
                if not stack: # daca stackul e gol, inseamna ca nu a inceput cu o paranteza macar, deci returnam FALSE 
                    return False

                if stack[-1] != matching[every_char]: # daca ultima paranteza deschisa e paranteza corecta pentru paranteza actuala de inchidere, daca nu e, returnam False
                    return False
                
                stack.pop() # daca stackul NU era gold si ce paranteza matching era corecta, automat, nu o mai adaugam pe cea de inchidere, ci ostergem pe cealalta de deschidere

            
        return len(stack) == 0

        
        
        
        
        
        
        
        
        # brackets = {'(',')','{','}','[',']'}
        # while s:

        #     if s[0] == '(':
        #         for every_char in reversed(s):
        #             if every_char in brackets and every_char != ')':
        #                 return False
        #             elif every_char == ')':
        #                 s = s[:-1]
        #                 return self.isValid(s)
        #             else:
        #                 s = s[:-1]

                        

        #     elif s[0] == '[':
        #         for every_char in reversed(s):
        #             if every_char in brackets and every_char != ']':
        #                 return False
        #             elif every_char == ']':
        #                 s = s[:-1]
        #                 return self.isValid(s)
        #             else:
        #                 s = s[:-1]

        #     elif s[0] == '{':
        #         for every_char in reversed(s):
        #             if every_char in brackets and every_char != '}':
        #                 return False
        #             elif every_char == '}':
        #                 s = s[:-1]
        #                 return self.isValid(s)
        #             else:
        #                 s = s[:-1]
        #     else:
        #         s=s[1:]


        # return True
