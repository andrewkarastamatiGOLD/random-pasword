import random 
simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
pass_length = int(input('Ведите длину вашего пароля:'))

zhocko = ''
for i in range(pass_length):
    zhocko += random.choice(simbols)
print(zhocko)