 #A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=8568
x4=(var_int%10)%2
x3=(var_int%100//10)%2
x2=(var_int%1000//100)%2
x1=(var_int//1000)%2
print(x1+x2+x3+x4)

