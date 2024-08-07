
def find_multiples(min_val, max_val, multiple_of, not_multiple_of):
    multiples = []
    for i in range(min_val, max_val + 1):
        if i % multiple_of == 0 and i % not_multiple_of != 0:
            multiples.append(i)
    return multiples

# Define the range and criteria
min_val = 2000
max_val = 2500
multiple_of = 17
not_multiple_of = 5
count=0

# Find the multiples
result = find_multiples(min_val, max_val, multiple_of, not_multiple_of)

# Print the results
print("Numbers between 2000 and 2500 that are multiples of 17 but not multiples of 5:")
for num in result:
    print(num)
    count=count+1
print("total numbers:")
print(count)



