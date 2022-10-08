#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".

var_int=4566
x4=(var_int%10)%2*var_int%10
x3=(var_int//10%10)%2*var_int//10%10
x2=(var_int//100%10)%2*var_int//100%10
x1=(var_int//1000)%2*var_int//1000 
sum_even=x1+x2+x3+x4
print(sum_even)