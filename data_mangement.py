#adding comments for assignment5
import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    e = float(sys.argv[4])
except ValueError:
    print("Inputs must be numbers")
    sys.exit(1)

numbers = [a,b,c,d,e]

if any(num < 0 for num in numbers):
    print("One or more values are negative")

avg = sum(numbers) / len(numbers)
avg_msg = "The avarage is grater then 50" if avg > 50 else "The avarage is less than 50"

pos = sum(1 for num in numbers if num > 0)
par = "It's even" if pos % 2 == 0 else "It's odd"

more_10 = sorted([num for num in numbers if num > 10])

print("Content-type: text/html\n")
print("<html><body>")
print("<h2>Data Management Results</h2>")
print("<p>Original Numbers: " + ", ".join(map(str, numbers)) + "</p>")
print("<p>Numbers Greater than 10 (Sorted): " + ", ".join(map(str, more_10)) + "</p>")
print("<p>Average: " + str(avg) + "</p>")
print("<p>" + avg_msg + "</p>")
print("<p>" + par + "</p>")
print("</body></html>")
