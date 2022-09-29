script nombre premier de 1 a 100.000

#affiche les premier
min = int(1)
max = int(100000)
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)

raté
