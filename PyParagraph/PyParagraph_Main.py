txt_path = "paragraph_1.txt"

with open(txt_path, 'r') as myfile:
    data=myfile.read().replace('\n', '')

# split the paragraph into letters
letter_list = list(data)
# calculate the number of letters
letter_count = len(letter_list)

# split the paragraph into words
word_list = data.split()
## calculate the number of words
word_count = len(word_list)
print(word_count)

## calculate the number of sentences
sent_list = data.split('.')
sen_count = len(sent_list)

## find the average letter count per word
avg_letter_count_word = letter_count / word_count

## find the average sentence length in words
avg_sentence_length_words = word_count / sen_count

print("Paragraph Analysis")
print("------------------")
print("Word count: " + str(word_count))
print("Sentence count: " + str(sen_count))
print("Average letter count: " + str(avg_letter_count_word))
print("Average sentence length: " + str(avg_sentence_length_words))



