#
# fizzbuzz.py
#

# Print all numbers from 1 to 100.
# If a particular number is a multiple of 3 then print "Fizz" instead of the number
# If a particular number is a multiple of 5 then print "Buzz" instead of the number
# If a particular number is a multiple of 3 and a multiple of 5 then print "FizzBuzz" instead of the number

for i in range(1,100)
    print(i)
    if i % 3 == 1:
        print("Fizz")
    elif i % 5 == 1:
        print("Buzz")
    elif i % 3 and i % 5 == 1:
        print("BuzzFizz")
