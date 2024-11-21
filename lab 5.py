# 1. Separate String into Comma-Separated Values
print("Comma-separated values:", "India.is.my.country".replace(".", ","))

# 2. Sort Strings Alphabetically
print("Sorted strings:", sorted(["banana", "apple", "cherry", "date"]))

# 3. Remove a Given Character from a String
print("String after removing 'A':", "M.A.N.I.P.A.L".replace("A", ""))

# 4. Remove Dots from a String
print("String after removing dots:", "M.A.N.I.P.A.L".replace(".", ""))

# 5. Reverse a User Input String
print("Reversed string:", input("Enter a string: ")[::-1])

# 6. Check if a String Contains Only Digits
print("Contains only digits:", input("Enter a string: ").isdigit())

# 7. Check if a String is Palindrome
s = input("Enter a string: "); print("Is palindrome:", s == s[::-1])

# 8. Count the Number of Vowels in a String
print("Number of vowels:", sum(1 for c in input("Enter a string: ").lower() if c in "aeiou"))

# 9. Check if Every Word in a String Starts with Capital Letters
print("All words start with capital letters:", all(word[0].isupper() for word in input("Enter a string: ").split()))
