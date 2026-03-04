country = "Saudi Arabia"
name = "Haydan"

letter = f"hey my names is {name} and I am from {country}"


print(letter.format(name,country))
print(letter)
print(letter)



# notes iss ko fstring kehte hai and iss may 49.213547 value hai to sirf 
# 2 values likhna hai (.) ke baat to .2f teen values cahiye to .3f 
# 4 values after point chahiye to .4f kar na padega 
# ek baat aur user ke te time column lagana bahut zaruri hai 
# for example: ---> 
# prize = 45.76458 ---> prize:.3f --> isse output mile ga 45.764

prize = 43.875692
print(type(prize))
print(type(f"The Prize is {prize:.10f}"))




# excercise

ticket_id = 452
issue="water Leakage"
priority = "High"

print(f"[LOG] Ticket # {ticket_id}: Issue is {issue} | Priority:{priority.upper()}")