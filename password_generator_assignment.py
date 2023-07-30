import random
import array

password_length=15
digits=['0','1','2','3','4','5''6','7','8','9']
lower_case= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case= ['A','B','C','D','E','F','G','H','I','J,','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols= ['!','@','#','$','%','^','&','*','(',')','-','+','=',':',';','?','/','<','>'',','|','{','}',]

combined_list= digits + lower_case + upper_case + symbols

rand_digits= random.choice(digits)
rand_lower_case= random.choice(lower_case)
rand_upper_case= random.choice(upper_case)
rand_symbols= random.choice(symbols)

generated_pass= rand_digits + rand_lower_case + rand_upper_case + rand_symbols

for i in range(password_length - 4):
    generated_pass= generated_pass + random.choice(combined_list)

    generated_pass_list= array.array('u', generated_pass)
    random.shuffle(generated_pass_list)
password = ""
for i in generated_pass_list:
    password = password + i
        
print(password)
