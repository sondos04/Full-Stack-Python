age = [11, 15, 18, 20, 25, 30]

def filtered_ages(age):
    return age >= 18

print(list(filter(filtered_ages, age)))