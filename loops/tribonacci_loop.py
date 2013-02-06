prompt = "Enter a natural number greater than 3"
limit = eval(raw_input(prompt))
(third, second, first, result) = 0, 0, 1, 0
for i in range(limit-2):
    result = first + second + third
    first = second
    second = third
    third = result
print "Tribonacci number " + str(limit)
print "Tribonacci value is: " + str(result)