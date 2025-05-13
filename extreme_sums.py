def sum_strings(x, y):

    #Dictionary for efficient type conversion
    to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    to_str_f = {0: '00', 1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09',
              10: '10', 11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17',
              18: '18', 19: '19'}

    len_x = len(x)
    len_y = len(y)

    #Evening strings of different length (12 and 1234 -> 0012 1234)
    if len_x > len_y:
        y = "0" * (len_x - len_y) + y
    elif len_x < len_y:
        x = "0" * (len_y - len_x) + x
    
    #If both values are empty then return 0
    if x == '': return '0'
        
    #Variable initializations
    str_len = len(x)
    pointer = str_len - 1
    carry = 0
    retrn_str = ""
    sum_ = 0
    sum_arr = []

    #Addition with strings
    while 0 <= pointer:
        sum_ = to_str_f[to_int[x[pointer]] + to_int[y[pointer]] + carry]
        carry = to_int[sum_[0]]
        sum_arr.append(sum_[1])
        pointer -= 1

    #Add the remaning carrier
    if carry != 0:
        sum_arr.append(to_str[carry])

    #Convert array to string reversed
    retrn_str = "".join(sum_arr[::-1])

    #Remove the zeroes at start of string
    retrn_str = retrn_str.lstrip('0')
    
    return "0" if retrn_str == "" else retrn_str
 
if __name__ == "__main__":

    with open("extreme_nr1.txt", "r") as f:
        value_a = f.read()

    with open("extreme_nr2.txt", "r") as f:
        value_b = f.read()

    sum = sum_strings(value_a, value_b)

    print(sum)