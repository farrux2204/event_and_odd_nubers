#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

a=5686
var_int=0

a1 = a%10
var_int=var_int+(a1+1)%2
a//=10 


a2 = a%10
var_int=var_int+(a2+1)%2
a//=10

a3 = a%10
var_int=var_int+(a3+1)%2
a//=10

a3 = a%10
var_int=var_int+(a3+1)%2
a//=10
print(var_int)