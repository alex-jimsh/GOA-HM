#creating list
words = ["Hello", "world", "alex", "is", "genuis"]

# Using the join to join them with space bar in between
sentence = " ".join(words)
print("Sentence after join:", sentence)
#Hello world alex is genuis

# Using the replace function to replace 'world' with 'there'
sentence_replaced = sentence.replace("world", "there")
print("Sentence after alex replace:", sentence_replaced)
# Output: Hello there alex is genuis
