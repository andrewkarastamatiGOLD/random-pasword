import random 
simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
pass_length = int(input('Ведите длину вашего пароля:'))

fgfg = ''
for i in range(pass_length):
    fgfg += random.choice(simbols)
print(fgfg)
