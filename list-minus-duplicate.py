user_input = input("Input String or number or both, separate them by comma: ")
input = user_input.split(",")

unrepeated_elements = []
seen = set()
for item in input:
    if item not in seen:
        unrepeated_elements.append(item)
        seen.add(item)

print("Output:", ', '.join(unrepeated_elements))
