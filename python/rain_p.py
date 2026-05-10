RAIN_TODAY = 0.6
RAIN_TOMORROW = 0.5
NO_RAIN_EITHER = 0.3


#The probability that it will rain today or tomorrow.
print("rain today or tomorrow:", 1 - NO_RAIN_EITHER)

#The probability that it will rain today and tomorrow.
print("rain today and tomorrow:", RAIN_TODAY + RAIN_TOMORROW - (1 - NO_RAIN_EITHER))

#The probability that it will rain today but not tomorrow.
print("rain today but not tomorrow:", RAIN_TODAY - (RAIN_TODAY + RAIN_TOMORROW - 1))

#The probability that it either will rain today or tomorrow, but not both.
print("rain today or tomorrow but not both:", RAIN_TODAY + RAIN_TOMORROW - 2 * (RAIN_TODAY + RAIN_TOMORROW - 1))