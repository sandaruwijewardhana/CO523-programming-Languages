values = [10, "5", 2.5]

for i in range(len(values)):
    for j in range(i + 1, len(values)):
        try:
            val1 = values[i]
            val2 = values[j]
            
            # Explicitly converting both operands to float to ensure mathematical addition
            # This handles mixtures of int, string-numbers, and floats safely.
            result = float(val1) + float(val2)
            
            print(f"{val1} ({type(val1).__name__}) + {val2} ({type(val2).__name__}) = {result} (type: {type(result).__name__})")
        except (TypeError, ValueError) as e:
            print(f"Error adding {values[i]} and {values[j]}: {e}")