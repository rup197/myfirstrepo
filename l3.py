#L3 - Create Python Console Application to randomly generate OTP kind of secure code
import random     #import random module
import string     #import string module

def generate_otp(length):  #define the function with the parameter length
    letters = string.ascii_letters + string.digits   #store upper & lower 
                                                    #character and digit in 'letters' variable
    otp = ''.join(random.choice(letters) for _ in range(length))
    return otp

otp_length = 8 #length of OTP
otp = generate_otp(otp_length) #generate OTP
print("generate OTP :",otp) #print OTP
