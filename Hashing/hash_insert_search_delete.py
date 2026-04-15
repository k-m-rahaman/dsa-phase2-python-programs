hash_table = {}

# Insert
hash_table[10] = "A"
hash_table[20] = "B"

# Search
key = 10
if key in hash_table:
    print("Found:", hash_table[key])
else:
    print("Not Found")

# Delete
del hash_table[10]

print("Hash Table:", hash_table)