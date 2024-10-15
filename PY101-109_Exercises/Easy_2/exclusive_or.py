# def xor(cond1, cond2):
#     match (bool(cond1), bool(cond2)):
#         case (True, True):
#             return False
#         case (False, False):
#             return False
#         case (True, False):
#             return True
#         case (False, True):
#             return True
        
def xor(cond1, cond2):
    if (cond1 and not cond2) or (not cond1 and cond2):
        return True
    
    return False
        
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)