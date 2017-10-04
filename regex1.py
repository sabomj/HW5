import re
hand = open('regex_sum_37002.txt').read()

numbers = re.findall('[0-9]+', hand)

print ('Sum of Numbers:',sum(int(x) for x in numbers))
