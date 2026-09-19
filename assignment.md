# Python Practice Problems
### Covering: Data Types & I/O · Operators · Conditions · Loops · Lists/Tuples/Sets/Dicts · Functions & Lambda

Work through these roughly in order — later sections lean on skills from earlier ones. Each problem lists the concepts it's meant to exercise.

---

## Part 1 — Data Types, Input & Output

**1.1 — Personal Introduction**
Ask the user for their name, age, and city using `input()`. Print a sentence introducing them, using an f-string.

**1.2 — Temperature Converter**
Ask the user for a temperature in Celsius. Convert it to Fahrenheit (`F = C * 9/5 + 32`) and print the result rounded to 1 decimal place.

**1.3 — Simple Calculator**
Ask the user for two numbers and an operator (`+`, `-`, `*`, `/`). Print the result. Handle division by zero with a friendly message instead of crashing.

**1.4 — Restaurant Bill**
Ask for the bill amount and a tip percentage (default 10% if left blank). Print the tip amount and total, formatted to 2 decimal places.

---

## Part 2 — Operators

**2.1 — Even or Odd**
Ask for a number and print whether it's even or odd, using the modulus operator.

**2.2 — Leap Year Checker**
Ask for a year and determine if it's a leap year. (Divisible by 4, but not by 100 unless also by 400.)

**2.3 — BMI Calculator**
Ask for weight (kg) and height (m). Compute BMI (`weight / height ** 2`) and print it formatted to 1 decimal place, along with the category (Underweight / Normal / Overweight) using comparisons.
<18 underweight 18-25-->Normal  25-30-->overweight >30 obese 

**2.4 — Swap Without a Third Variable**
Ask for two numbers and swap their values without using a temporary variable. (Hint: tuple packing/unpacking.)

---

## Part 3 — Conditions

**3.1 — Grade Classifier**
Ask for a score (0–100) and print a letter grade using `if / elif / else` (A ≥ 90, B ≥ 75, C ≥ 60, else F).

**3.2 — Triangle Type**
Ask for three side lengths. Determine if they form a valid triangle, and if so, whether it's equilateral, isosceles, or scalene.

**3.3 — Simple Login Check**
Store a username and password. Ask the user to log in. Use nested conditions to give a specific message for "wrong username," "wrong password," and "success." Ask repeatedly until both the username and password are right.

**3.4 — FizzBuzz (single number)**
Ask for a number. Print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if both, otherwise the number itself.

---

## Part 4 — Loops

**4.1 — Multiplication Table**
Ask for a number and print its multiplication table from 1 to 10 using a `for` loop.

**4.2 — Sum of Natural Numbers**
Ask for a number `n` and use a `while` loop to compute the sum of all natural numbers from 1 to `n`.

**4.3 — Prime Number Finder**
Ask for a number `n` and print all prime numbers from 2 up to `n`.

**4.4 — Reverse a String**
Ask for a word and print it reversed — without using slicing (`[::-1]`) or the built-in `reversed()`. Use a loop instead.

**4.5 — Vowel Counter**
Ask for a sentence and count how many vowels it contains, using a loop and the `in` operator.

**4.6 — FizzBuzz (1 to N)**
Loop from 1 to a number `n` the user provides, applying the FizzBuzz rule from 3.4 to every number.

---

## Part 5 — Lists, Tuples, Sets & Dictionaries

**5.1 — Manual Max and Min**
Given a list of numbers, find the largest and smallest values *without* using `max()` or `min()`. Loop through the list yourself.

**5.2 — Remove Duplicates**
Given a list with repeated values, produce a new list with duplicates removed, preserving order. Try it two ways: with a loop, and with a set.

**5.3 — Merge Two Dictionaries**
Given two dictionaries of product prices, merge them into one. If a product exists in both, keep the higher price.

**5.4 — Word Frequency Counter**
Given a sentence, build a dictionary that counts how many times each word appears (case-insensitive).

**5.5 — Class Topper**
Given a list of tuples like `[("Sita", 88), ("Ram", 95), ("Maya", 91)]`, find and print the name and score of the student with the highest score — without using `sorted()` or `max()`.

**5.6 — Shopping Cart**
Represent a shopping cart as a list of dictionaries (`{"item": ..., "price": ..., "qty": ...}`). Write code that loops through the cart and prints an itemized receipt plus a grand total.

---

## Part 6 — Functions & Lambda

**6.1 — Palindrome Checker**
Write a function `is_palindrome(word)` that returns `True` or `False`. Test it on "level", "hello", and "racecar".

**6.2 — Simple Interest**
Write a function `simple_interest(principal, rate, years=1)` with a default value for `years`, returning the interest earned.

**6.3 — Variable-Length Max**
Write a function `my_max(*numbers)` that returns the largest of any number of arguments passed in, without using the built-in `max()`.

**6.4 — Sort by Custom Key**
Given a list of dictionaries representing people (`{"name": ..., "age": ...}`), use `sorted()` with a `lambda` to sort them by age.

**6.5 — Map and Filter**
Given a list of numbers, use `map()` with a lambda to square every number, then use `filter()` with a lambda to keep only the even results.

---

## Part 7 — Capstone Challenges
*(Combine everything above — these are meant to take longer.)*

**7.1 — Student Gradebook**
Store several students as a dictionary mapping name → list of scores. Write functions to:
- compute a student's average score
- assign a letter grade from that average
- print every student sorted from highest to lowest average (use a lambda as the `sorted()` key)

**7.2 — Contact Book**
Build a simple command-line contact book using a dictionary (name → phone number):
- Show a menu in a loop: Add, Search, Delete, List All, Quit
- Use functions for each action
- Keep looping until the user chooses Quit

**7.3 — Number Guessing Game**
The program picks a secret number (hardcode one). Loop, asking the user to guess:
- Print "Too high" / "Too low" / "Correct!" using conditions
- Count how many guesses it took
- Use `break` to end the loop on a correct guess, and the loop's `else` to print a message if you'd like to add a guess limit

---

### How to use this set
Try each problem without looking at the concepts list first — treat it as a hint if you get stuck. Aim to solve Parts 1–4 comfortably before starting Part 5, and don't attempt the capstones until Part 6 feels solid.