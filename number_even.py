#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

var_int=1113
a=0


var_int1 = a%10
a==a+(var_int1+1)%2
a//=10 



var_int2 = a%10
a=a+(var_int2+1)%2
a//=10


var_int3 = a%10
a=a+(var_int3+1)%2
a//=10


var_int4 = a%10
a=a+(var_int4+1)%2
a//=10

print(a)