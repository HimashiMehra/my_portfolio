a, b, c, d = 15, 30, 10, 25

if a >= b and a >= c and a >= d:
    m1 = a
    if b >= c and b >= d:
        m2 = b
        if c >= d: m3, m4 = c, d
        else: m3, m4 = d, c
    elif c >= b and c >= d:
        m2 = c
        if b >= d: m3, m4 = b, d
        else: m3, m4 = d, b
    else:
        m2 = d
        if b >= c: m3, m4 = b, c
        else: m3, m4 = c, b

elif b >= a and b >= c and b >= d:
    m1 = b
    if a >= c and a >= d:
        m2 = a
        if c >= d: m3, m4 = c, d
        else: m3, m4 = d, c
    elif c >= a and c >= d:
        m2 = c
        if a >= d: m3, m4 = a, d
        else: m3, m4 = d, a
    else:
        m2 = d
        if a >= c: m3, m4 = a, c
        else: m3, m4 = c, a

elif c >= a and c >= b and c >= d:
    m1 = c
    if a >= b and a >= d:
        m2 = a
        if b >= d: m3, m4 = b, d
        else: m3, m4 = d, b
    elif b >= a and b >= d:
        m2 = b
        if a >= d: m3, m4 = a, d
        else: m3, m4 = d, a
    else:
        m2 = d
        if a >= b: m3, m4 = a, b
        else: m3, m4 = b, a

else:
    m1 = d
    if a >= b and a >= c:
        m2 = a
        if b >= c: m3, m4 = b, c
        else: m3, m4 = c, b
    elif b >= a and b >= c:
        m2 = b
        if a >= c: m3, m4 = a, c
        else: m3, m4 = c, a
    else:
        m2 = c
        if a >= b: m3, m4 = a, b
        else: m3, m4 = b, a

print(f"1st Max: {m1}")
print(f"2nd Max: {m2}")
print(f"3rd Max: {m3}")
print(f"4th Max: {m4}")