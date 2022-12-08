import random

class Password:
    symbols = "1234567890-=!@#$%^&*()_+qwertyuiop[]\asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM"
    def __init__(self, numbers, length, upperCase = True, lowCase = True, digits = True):
        self.numbers = numbers
        self.length = length
        self.upperCase = upperCase
        self.lowCase = lowCase
        self.digits = digits
    def generate_password(self):
        str_all = self.symbols
        if self.digits == False:
            str_all = ''.join(item for item in str_all if item.isalpha())
        if self.upperCase == False:
            str_all = ''.join(item for item in str_all if not item.isupper())
        if self.lowCase == False:
            str_all = ''.join(item for item in str_all if not item.islower())
        for number in range(self.numbers):
            password = ''
            for x in range(self.length):
                password += random.choice(str_all)
            print(password)


helper = Password(5,5,False, True, True)
helper.generate_password()

