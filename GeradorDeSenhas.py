from random import randint, choice

word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
quantidade = int(input('Quantas letrar tera a senha?\n>:'))
i = 0
q = ""

while i < quantidade:
    i = i+1
    q = q + word[randint(1,25)] 
    if randint(0,20) <= 7:
        q = q.upper()
    if randint(0,20) <= 7:
        q = q.lower()
print(q)