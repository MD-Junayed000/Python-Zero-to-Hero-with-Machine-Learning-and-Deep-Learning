# indexing = accessing elements of a sequence using []

credit_number="1234-3456-2347"
print(credit_number[0])
print(credit_number[4:8])
# when use colon==[start:end:step]
# from 4 index too last
print(credit_number[4:])
# negetive comes from last starting from -1 as index
print(credit_number[-1])
# when use colon==[start:end:step]
# everything from begining to end just in step 2
print(credit_number[::2])
# show only the last four digits
last_digit=credit_number[-4:]# [start:end]
print(f"xxxx-xxxx-xxxx-{last_digit}")

# credit-number in reversal order
reversal= credit_number[::-1]#from starting to last in reverse step
print(reversal)