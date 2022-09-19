# Project Euler Problem 17
# Number Letter Counts

n = 1000
total = 0

options = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
           8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
           13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
           18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
           100: 'hundred', 1000: 'thousand', '&': 'and'}

for i in range(n):
    if len(str(i)) == 3:
        total += len(options[int(str(i)[0])]) + len(options[100])
        if str(i)[1:] != '00':
            total += len(options['&']) 
            if 10 < int(str(i)[1:]) < 20:
                total += len(options[int(str(i)[1:])])
            else:
                total += len(options[int(str(i)[-2]+'0')]) + len(options[int(str(i)[-1])])
    if len(str(i)) == 2:
        if 10 < i < 20:
            total += len(options[i])
            #print(options[i])
        else:
            total += len(options[int(str(i)[-2]+'0')]) + len(options[int(str(i)[-1])])
            #print(options[int(str(i)[-2]+'0')]+options[int(str(i)[-1])])
    if i < 10:
        total += len(options[i])
        #print(options[i])

total += len(options[1]) + len(options[1000])

print(total)
    
