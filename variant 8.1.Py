def number(n):
    for d in str(n):
        if d == '0' or n%int(d):
            return False
    return True
for i in range(1, int(input()) + 1):
    if number(i):
      print(i) 
    
    