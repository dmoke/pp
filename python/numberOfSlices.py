# Kata: Series Slices
# Given a string of digits and a slice size n, extract all consecutive n-digit slices from the string.
# For example, the string "01234" with n=2 has slices: [0, 1], [1, 2], [2, 3], [3, 4]

def series_slices(digits, n):
   if n > len(digits):
      raise ValueError("n must be less than or equal to the length of digits") 
   result = [[*[int(d) for d in digits][i: i + n]] for i in range(len(digits))]
   return [s for s in result if len(s) == n]






print(series_slices("01234", 2))