def Lkubus(s):
    return s * s * s

def Lbalok(s, t):
    return s * s * t

def Ltabung(r, t):
    return 3.14 * r * r * t

def Lkerucut(r, t):
    return (1/3) * 3.14 * r * r * t

def Lprisma(l, w, t):
    return l * w * t

print(Lprisma(2,3,4))
print(Lkerucut(2,4))
print(Ltabung(2,4))
print(Lbalok(2,4))
print(Lkubus(2))