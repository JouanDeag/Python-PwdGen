import random
all = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
length = int(input("Input Desired Length: "))

loop = 0
pwd = ""
while loop < length:
    number = random.SystemRandom().randint(0, 75)
    pwd += all[number]
    loop += 1
    
print(f"Your Password is: {pwd}")
