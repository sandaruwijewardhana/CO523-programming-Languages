def function_c(z):
    print(f"  → ENTER function_c(z={z})")
    result = z * 2
    print(f"    Computing: {z} * 2 = {result}")
    print(f"  ← EXIT function_c, returning {result}")
    return result


def function_b(y):
    print(f"  → ENTER function_b(y={y})")
    print(f"    Calling function_c({y + 1})...")
    result = function_c(y + 1)
    final = result + 5
    print(f"    Computing: {result} + 5 = {final}")
    print(f"  ← EXIT function_b, returning {final}")
    return final


def function_a(x):
    print(f"  → ENTER function_a(x={x})")
    print(f"    Calling function_b({x * 2})...")
    result = function_b(x * 2)
    print(f"  ← EXIT function_a, returning {result}")
    return result


final_result = function_a(3)
print(f"\nFinal result: {final_result}")