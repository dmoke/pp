
from probability import bayes_binary


chance_of_rain = bayes_binary(
    p_h=0.30,                 # prior chance of rain
    p_e_given_h=0.85,         # dark clouds if rain
    p_e_given_not_h=0.20,     # dark clouds without rain
)

print(chance_of_rain)

chance_of_librarian = bayes_binary(
    p_h=1/21,                 
    p_e_given_h=0.4,        
    p_e_given_not_h=0.1,   
)

print(chance_of_librarian)