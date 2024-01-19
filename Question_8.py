#Abdul Muizz

#Question No. 8:
#Define a complex number variable, comp_num, with a real and imaginary part. Print both parts separately.

#First we declare a complex number variable "comp_num" and assign it a complex value with complex function.
comp_num = complex(1.0,2.0)

#Now we seprate real and imaginary part by .real and .imag function in variables . 
real_part = comp_num.real
imaginary_part = comp_num.imag

#Now we  print them using print function.
print("The real part is :",real_part)
print("The imaginary part is :",imaginary_part)