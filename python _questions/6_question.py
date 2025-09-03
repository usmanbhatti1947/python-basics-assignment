# User will input (3ages).Find the oldest one

def find_oldest_age(ages):
    # Find the maximum age from the list of ages
    return max(ages)

ages = [25, 30, 22]
oldest = find_oldest_age(ages)
print(f"The oldest age is: {oldest}")
