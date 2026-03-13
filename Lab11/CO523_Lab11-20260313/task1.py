import gc

class LabObject:
    def __init__(self, name):
        self.name = name
        print(f"Object '{self.name}' created.")

    def __del__(self):
        print(f"Object '{self.name}' is being deleted from memory.")

# 1. Create multiple objects
obj1 = LabObject("Alpha")
obj2 = LabObject("Beta")
obj3 = LabObject("Gamma")

# 2. Delete one of the objects using 'del'
print("\n--- Deleting obj1 ---")
del obj1 

# 3. Force garbage collection
print("\n--- Triggering manual garbage collection ---")
collected = gc.collect()
print(f"Garbage collector: collected {collected} objects.")