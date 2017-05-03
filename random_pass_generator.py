import os
import random
import string
import random


# estimated length of the password between 18-32 characters long
length = random.randint(18,32)

# uncomment below to see the length of the password
# print (length)

#creating the password with mix of characters and numbers
chars = '!@#$%^&*()'+ string.ascii_letters + string.digits + '!@#$%^&*()' 

#os.urandom outputs indistinguishable values to random generator
random.seed(os.urandom(1024))

#print the password
print (''.join(random.choice(chars) for i in range(length)))
