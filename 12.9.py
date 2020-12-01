# Anthony Guzman            12.9                CIS2348		1503239
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except Exception as ex:
        age = 0
    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]