import gc

class Demo:
    def __init__(self):
        self.ref = self

gc.disable()
print("Automatic GC enabled:", gc.isenabled())

obj = Demo()
del obj

print("Garbage collected:", gc.collect())

gc.enable()
print("Automatic GC enabled:", gc.isenabled())
