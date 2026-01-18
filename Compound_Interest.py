"""
Compound Interest Calculation
Amount=P(1+R/100)**T
ci=Amount-Principal
"""

Principal=float(input("Enter the Principal amount:"))
Rate=float(input("Enter the rate:"))
Time=float(input("Enter the time:"))

Amount=Principal*(1+Rate/100)**Time
Ci=Amount-Principal

print("Compound interest is",round(Ci,2))
