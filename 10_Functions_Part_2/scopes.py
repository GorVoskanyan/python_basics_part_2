# LEGB -> local, enclosed, global, built-in

x = 'global x'

def f():
    # global x
    x = 'enclosed x'
    def f2():
        nonlocal x
        x = 'local x'
        print(x)
    f2()
    print(x)


f()
print(x)