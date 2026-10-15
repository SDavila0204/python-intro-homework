#'not true' is false and 'false' is false
print(not True and False)

#'True' is true, and 'false and false' is false, but only one needs to be true due to the 'or' so it is true
print(True or False and False)

#5 is less than 3, which is true but not makes the statement 'not true', therefore it is false
print(not (5 > 3))

#10 equals 10 is true but 4 does not equal 4 is false, therefore it is false
print(10 == 10 and 4 != 4)

#not false is true and not true is false, but since it is an 'or' only one needs to be true, so the answer is true
print(not False or not True)
