import string
#this function is to convert only alphabets to lower cases(if any)
def lower_case(input_string) :
    input_string = list(input_string)
    print(input_string)
    for i in range(len(input_string)) :
        if 64 < ord(input_string[i]) < 91 :
            input_string[i] = chr( ord(input_string[i]) + 32 )  # 122 is when lower cases start in ASCII
    input_string = ''.join(input_string)
    return input_string

def main() :
    input_string = input()
    print('THe lower case of the string is.... ' + lower_case(input_string))

if __name__ == '__main__' :
    main()

