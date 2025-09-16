pattern = int(input('Enter the size of the pattern: '))
count =0

while count<pattern:
    for p in range(pattern):
        print('*', end="")
    count +=1
    print()