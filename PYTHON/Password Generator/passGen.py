import random
from secrets import choice
import string

length = int(input('Enter password length: '))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for i in range(length))
print('Your password is: ', password)