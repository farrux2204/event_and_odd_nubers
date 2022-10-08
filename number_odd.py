#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=1237

x=0

var_int1=var_int%10

x=x+(var_int1)%2

var_int//=10


var_int2=var_int%10

x=x+(var_int2)%2

var_int//=10


var_int3=var_int%10

x=x+(var_int3)%2

var_int//=10


var_int4=var_int%10


x=x+(var_int4)%2

var_int//=10

print(x) 