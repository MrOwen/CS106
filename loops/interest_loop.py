(principle, interest_rate, time) = 0, 5, 0
prompt = "Enter the principle"
principle = eval(raw_input(prompt))
prompt = "Enter the number of years"
time = eval(raw_input(prompt))
for i in range(1, time+1):
    principle = (1 + (interest_rate / 100.0)) * principle
    print "Current amount: $%.2f" % principle
print "Final amount: $%.2f" % principle