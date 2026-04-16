s = "Hello World"

vowels = consonants = spaces = 0

for ch in s:
    if ch == " ":
        spaces += 1
    elif ch.lower() in "aeiou":
        vowels += 1
    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)