def find_fractions():
    for numerator in range(1, 10000000):  
        for denominator in range(1, 10000000):  
            if numerator > denominator:  
                continue
            num_str = str(numerator)
            denom_str = str(denominator)
            for i in range(len(num_str)):
                if num_str[i] in denom_str:

                    new_num_str = num_str.replace(num_str[i], '', 1)
                    new_denom_str = denom_str.replace(denom_str[i], '', 1)

                    while num_str[i] in new_num_str and denom_str[i] in new_denom_str:
                        new_num_str = new_num_str.replace(num_str[i], '', 1)
                        new_denom_str = new_denom_str.replace(denom_str[i], '', 1)

                    if not new_num_str or not new_denom_str:
                        print(f"Found fraction: {numerator}/{denominator}")
                        return numerator, denominator  
find_fractions()
