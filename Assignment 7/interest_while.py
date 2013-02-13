(principle, interest_rate, future, years) = 0, 0, 0, 0
prompt = "Enter the principle: "
principle = eval(raw_input(prompt))
prompt = "Enter the interest rate: "
interest_rate = eval(raw_input(prompt))
prompt = "Enter the future value: "
future = eval(raw_input(prompt))
while principle <= future:
    principle = (1 + (interest_rate / 100.0)) * principle
    years += 1
print "%(years)i years will be needed before loan is worth $%(loan).2f" % \
      {'years': years, "loan": principle}
