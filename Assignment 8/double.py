(orig_principle, running_principle, interest_rate, years) = 1, 1, 0, 0
prompt = "Enter the interest rate: "
interest_rate = eval(raw_input(prompt))
while running_principle <= orig_principle * 2:
    running_principle = (1 + (interest_rate / 100.0)) * running_principle
    years += 1
print "At a %(interest_rate).1f%% interest rate, it will take %(years)i years to\
 double the amount" % {'interest_rate': interest_rate, 'years': years}
