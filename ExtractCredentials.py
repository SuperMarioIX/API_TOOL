with open('credentials.txt', 'r') as file:
    line1 = file.readline().strip()
    key1, value1 = line1.split('=')
    username = value1.strip()

    line2 = file.readline().strip()
    key2, value2 = line2.split('=')
    password = value2.strip()