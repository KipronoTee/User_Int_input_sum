# Use list comprehension to filter words with odd number of characters

def filter_odd_character_words(word_list):
    odd_character_words = [word for word in word_list if len(word) % 2 != 0]
    return odd_character_words

# creat word_list to filter
word_list = ["try",  "local","team", "norms", "football", "players"]
result = filter_odd_character_words(word_list)

# print  results 
print("Original list:", word_list)
print("Words with odd characters:", result)