data = [1, "2", 3.0, "hello"]
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        try:
            result = data[i] + data[j]
            print(f"{data[i]} + {data[j]} = {result} (type: {type(result)})")
        except TypeError as e:
            print(f"Cannot add {data[i]} ({type(data[i])}) + {data[j]} ({type(data[j])}): {e}")