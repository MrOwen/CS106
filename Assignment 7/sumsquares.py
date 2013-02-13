total = 0
input = 'yes'
while input == 'yes':
    prompt = "Enter a value>> "
    input = eval(raw_input(prompt))
    total += input ** 2
    input = raw_input("Continue (yes/no)?>> ")
print "The result of the sum of the squared values is: " + str(total)
