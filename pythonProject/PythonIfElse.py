n = int(input().strip())

if (n %  2 != 0):
    print("Weird")
elif (n % 2 == 0 & 2 <= n & n <= 5):
    print("Not Weird")
elif (n % 2 == 0 & 6 <= n & n <= 20 ):
    print("Weird")
else:
    print("Not Weird")
