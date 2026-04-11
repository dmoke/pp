#https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/solutions/java
def ho(func=""):
    return  "Ho!"+ func if func =="" else "Ho "+ func

print(ho(ho(ho())))