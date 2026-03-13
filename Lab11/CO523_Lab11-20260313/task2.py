import gc
import sys

class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student object '{self.name}' created.")

    def __del__(self):
        print(f"Student object '{self.name}' is being removed from memory.")

# 1. Create a list containing several objects
print("--- Initializing List ---")
student_list = [Student("Kamal"), Student("Nimal"), Student("Sunil")]

# 2. Show reference count (optional but helpful for observation)
# sys.getrefcount returns actual count + 1 (temporary reference)
print(f"Reference count for student_list[0]: {sys.getrefcount(student_list[0])}")

# 3. Remove references to some objects
print("\n--- Removing references to Kamal and Nimal ---")
student_list[0] = None  # Removes reference to "Kamal"
student_list.pop(1)     # Removes reference to "Nimal" by popping index 1

# 4. Call the garbage collector
print("\n--- Manually calling gc.collect() ---")
gc.collect()

print("\n--- End of script ---")