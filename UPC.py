def upc(code):
     code = pad_eleven(code)
     check_digit = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[
     check_digit = 3 * check_digit
     check_digit = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + check_dig
     if (check_digit % 10 == 0):
         return 0
     else:
         return (10 - (check_digit % 10))
         
         
def pad_eleven(code):
  return format(code, '011')


test1 = 4210000526
test2 = 3600029145
test3 = 12345678910
test4 = 1234567
print(upc(test1))
print(upc(test2))
print(upc(test3))
print(upc(test4))
