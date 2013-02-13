prompt = "Enter a natural number greater than 1: "
limit = eval(raw_input(prompt))
(first, second, third, result, counter) = 0, 1, 1, 0, 4
while result < limit:
    result = first + second + third
    first = second
    second = third
    third = result
    counter += 1
print "Tribonacci value: " + str(result)
print "Tribonacci index of that value: " + str(counter)
