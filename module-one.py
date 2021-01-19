
def check_speed(speed, roadtype):
    
    if speed < 0:
        raise ValueError('speed must be non-negative') 
    if roadtype not in ["highway", "city", "road"]:
        raise ValueError("the roadtype must be specified") 

    if roadtype == "highway" and speed < 30:
        return False
    elif roadtype == "highway":
        return True
    elif roadtype == "city" and speed <= 60:
        return True
    elif roadtype == "road" and speed <= 90:
        return True
    else: 
        return False


print ("\n-20, city  > ValueError")
try:
  print(check_speed(-20, "city"))
except ValueError as error:
  print(error)


print ("\n40, highway -> True")
print(check_speed(40, "highway"))


print ("\n90, city -> False")
print(check_speed(90, "city"))

print("\n90, highway -> True")
print(check_speed(90, "highway"))

print("\n50, table -> ValueError")
try:
  print(check_speed(50, "table"))
except ValueError as error:
  print(error)
