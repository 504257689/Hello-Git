import gmpy2
'''
mpz：用于表示大整数。
mpq：用于表示大分数（有理数）。
mpfr：用于表示浮点数。
mpc：用于表示复数。
'''
a=str(input('a='))
b=str(input('b='))
num1 = gmpy2.mpz(a)
num2 = gmpy2.mpz(b)
print("The product is:", num1 * num2)
