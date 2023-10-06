a: str = "b"
b: str = "c"
c: str = a

a = b
b = c

if c == a:
    print("red")
else:
    print("blue")