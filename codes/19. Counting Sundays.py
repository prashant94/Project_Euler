# Project Euler Problem 19
# Counting Sundays

from datetime import date

total_sundays = 0

def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range( ym_start, ym_end ):
        y, m = divmod( ym, 12 )
        yield y, m+1

for year,month in month_year_iter(1,1901,12,2000):
    if date(year,month,1).isoweekday() == 7:
        total_sundays += 1

print(total_sundays)





