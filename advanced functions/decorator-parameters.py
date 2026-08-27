def double(fn):
    def inner(*args, **kwargs):
         return fn(*args, **kwargs)
    return inner

@double
def merhaba():
    print("")

@double
def selam(isim):
    print("Selam", isim) 

@double
def iyigunler():
    return "iyi günler"

merhaba()
selam("Ali")
print(iyigunler())

