import random
import string

def get_custom_uid():
    new_uuid = \
    str(round((random.random()*25)+97)) +\
    str(round((random.random()*25)+97)) +\
    str(''.join(random.sample(string.ascii_uppercase+string.digits,10))) +\
    str(round((random.random()*25)+97)) +\
    str(round((random.random()*25)+97)) +\
    str(round((random.random()*25)+97)) +\
    str(''.join(random.sample(string.ascii_uppercase+string.digits,10))) +\
    str(round((random.random()*25)+97)) +\
    str(round((random.random()*25)+97))

    return new_uuid 
	
def get_custom_alpha_uid():
    alpha_uid = ''.join(random.sample((((string.ascii_uppercase+string.digits)*25)),6))

    return alpha_uid