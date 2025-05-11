def count_words(text):
    text = text.lower()           # Step 1: Make it lowercase
    words = text.split()          # Step 2: Split into words (watch out for punctuation!)
    
    word_count = {}               # Step 3: Prepare an empty dictionary
    
    for word in words:            # Step 4: Loop through each word
        # Step 5: Update the count in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count             # Step 6: Return the result

user_input=input("entre a text: ")
result=count_words(user_input)
print(result)