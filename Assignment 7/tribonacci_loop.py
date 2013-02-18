import math
prompt = "Enter a number: "
input = eval(raw_input(prompt))
incrementer = 2
while float(input) % incrementer != 0 and (2 <= incrementer <= math.sqrt(input)):
    print "incrementer is: ", incrementer
    incrementer += 1
if input % input == 0:
    print "Number is divisible by ", incrementer
else:
    print "Number is prime"
print math.sqrt(5)
print float(29) % 6
