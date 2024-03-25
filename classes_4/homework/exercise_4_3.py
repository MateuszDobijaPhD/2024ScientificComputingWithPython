# Create the following infinite generators:
# (a) iter_even(), producing even numbers (0, 2, 4, ...),
# (b) iter_odd(), producing odd numbers (1, 3, 5, ...),
# (c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).

def iter_even():   # an infinite iterator
    i = 0
    step = 2
    while True:
        yield i
        i += step


def iter_odd():   # an infinite iterator
    i = 1
    step = 2
    while True:
        yield i
        i += step


def iter_power(k):   # an infinite iterator
    i = 1
    while True:
        yield i
        i *= k

print("even gen:")
evenGen = iter_even()
for i in evenGen:
    print(i)
    if i > 100:   # we have to break the loop manually
        break

print("\nodd gen:")
oddGen = iter_odd()
for i in oddGen:
    print(i)
    if i > 100:   # we have to break the loop manually
        break

print("\npower gen:")
k = 2
powerGen = iter_power(k)
for i in powerGen:
    print(i)
    if i > 100:   # we have to break the loop manually
        break