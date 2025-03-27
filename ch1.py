#e_prev = 0
#n = 1
#e = (1 + 1 / n) ** n
#tolerance = 0.000000001

#while e - e_prev > tolerance:
#    e_prev = e
#    n += 1
#   e = (1 + 1 / n) ** n
#


tolerance = 0.000000001
:wq


e_prev = 0

for n in range(1, 100000):
    e = (1 + 1 / n) ** n
    if e - e_prev < tolerance:
        break
    e_prev = e

print(f"(1 + 1 / n) ** n is about {e} when n = {n}.")
