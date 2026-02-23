def factorial(n, depth=0):
    indent = "  " * depth
    print(f"{indent}→ CALL factorial({n}) [Depth: {depth}]")

    if n <= 1:
        print(f"{indent}  Base case reached!")
        print(f"{indent}← RETURN 1")
        return 1

    print(f"{indent}  Recursive call: factorial({n-1})")
    result = n * factorial(n - 1, depth + 1)
    print(f"{indent}  Computed: {n} * {result // n} = {result}")
    print(f"{indent}← RETURN {result}")
    return result


result = factorial(5)
print(f"\nFinal Result: 5! = {result}")