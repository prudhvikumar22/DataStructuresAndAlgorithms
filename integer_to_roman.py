roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def int_to_roman(decimal):
    result = ''
    for numeral, number in roman_numeral_map:
        print(number, numeral)
        while decimal >= number:
            print(decimal)
            result += numeral
            decimal -= number
            print('subtracting {0} from input, adding {1} to output'.format(number, numeral))
    return result


number = input("Enter the decimal: ")
print(int_to_roman(decimal=int(number)))