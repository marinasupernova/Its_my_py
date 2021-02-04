import re

s = '''Уважаемые! Если вы к 09:00 не вернёте 
чемодан, то уже в 09:00:01 я за себя не отвечаю. 
PS. С отношением 25:50 всё нормально!'''

result = re.sub("(2[0-3])|([0-1][0-9]):[0-5][0-9](:[0-5][0-9])?", '(TBD)', s)

print(result)





# def check_time(t1, t2):
#         if t1 in [0, 1, 2]:
#             if t1 == 2:
#                 if t2 < 4:
#                     return True
#                 else:
#                     return False
#             else:
#                 return True
#         else:
#             return False 
   

# print(check_time(0,9)) 
# print(check_time(1,4))    
# print(check_time(1,9))    
# print(check_time(2,4))
# print(check_time(3,1))        