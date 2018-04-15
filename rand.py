import random

class randomize_all:

    def __init__(self, boon):
        self.new_email = boon

    def generate_email(self):
        self.string = 'qwertyuioplkjhgfdsazxcvbnm1230456789'
        self.listt = list(self.string)
        self.new_email =''.join([random.choice(self.listt) for x in range(10)])
        self.boon = self.new_email+'@domail.com'
        print(self.boon)
        return self.boon

    def generate_phone(self):
        self.y = (random.randint(1,9)) % 2
        if self.y == 0:
            self.phone = '909' + (''.join([str(random.randint(0,9)) for x in range(7)]))
        elif self.y == 1:
            self.phone = '925' + (''.join([str(random.randint(0,9)) for x in range(7)]))
        print (self.phone)

#test = randomize_all.generate_phone(N)
