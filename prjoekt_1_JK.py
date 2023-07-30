#ohlášení o nahrávání modul TEXTS z balíčka(knihovny) task_templ_JK
from task_templ_JK import TEXTS

separator = '-' * 40

users = {
     'bob': '123',
     'ann': 'pass123',
     'mike': 'password123',
     'liz': 'pass123',
 }
 
 #2. Vyžádá si od uživatele přihlašovací jméno a heslo
username = input('username: ')
password = input('password: ')

#3. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
#4. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
#5. pokud není registrovaný, upozorni jej a ukonči program.**
if username in users and users[username] == password:
	print(separator)
	print('Welcome to the app,', username, '\nWe have 3 texts to be analyzed')
	print(separator)
else:
    print('$ python projekt1.py\nusername:' + username + '\npass:' + password + '\nunregistered user,terminating the program..')
    quit()  

#5_a Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS :
#Pokud uživatel vybere takové číslo textu, které není v zadání, program jej
#upozorní a skončí,
#pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
try:
    text = int(input('Enter a number btw. 1 and 3 to select: ')) - 1
except ValueError:
    print('not a number, terminating the program..')
    quit()  
    
if text < 0 or text  > 2:
	print('Enter a number that is not btw. 1 and 3, terminating the program..')
	quit()	
else:  
	 print(separator)
	 
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
for char in TEXTS[text]:
   if char not in punctuations:
       no_punct = no_punct + char

t = (no_punct.split())

#počet slov
print('There are', len(t) , 'words in the selected text.')

#počet slov začínajících velkým písmenem
#print(f'There are {sum(i.istitle() for i in t)} titlecase words')
print('There are', sum(i.istitle() for i in t), 'titlecase words')

#počet slov psaných velkými písmeny
print('There are', sum((i.isupper() and i.isalpha()) for i in t), 'uppercase words')

#počet slov psaných malými písmeny,
print('There are', sum((i.islower() and i.isalpha()) for i in t), 'lowercase words')

#počet čísel (ne cifer) a sumu všech čísel (ne cifer) v textu
num_list = []
sum = n = 0
for i in t:
    if i.isdigit():
        sum += int(i)
        n += 1
print ('There are', n, 'numeric strings.\nThe sum of all the numbers', sum)
print(separator)

#Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu
a = []
for i in t:
  a.append(len(i))
  
print('LEN|      OCCURENCES      |NR.')
print(separator)

d = {}
for item in a:
    if item in d:
        d[item] = d.get(item) + 1
    else:
        d[item] = 1

for k,v in d.items():
	sk = ' ' + str(k)
	sv = '*' * v + ' ' * 20
	print(sk[-2:], '|', sv[:20], '|', v)