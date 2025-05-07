def func(r, p, n):
    s = ""
    c = 0
    while p < len(r) and c < n:
        if p >= 2:
            s += r[p]
            c += 1
        p += 1
    return s

d = 2
a = input("Ingrese su rol (incluído el guión y el dígito verificador): ")
b = int(input("Ingrese el día real de su cumpleaños (entre 1 y 31): "))
c = b%3
if c == 1:
    c = c*4
elif c == 2:
    c = c*3
    d = c/2
r = func(a, c, d)
print(r)