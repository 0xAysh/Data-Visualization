from die import Die

# Create a D6.

die = Die() # Make some rolls, and stores results in a list.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
freqs = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    freq = results.count(value)
    freqs.append(freq)

print(freqs)