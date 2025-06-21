import string
import re

file_path = 'article.txt'
  
with open(file_path, 'r') as file:
  file_content = file.read() #article.txt as a string, stored in file_content

translator = str.maketrans('', '', string.punctuation)
text = file_content.translate(translator)  #removes punctuation 
clean_text = re.sub(r'[^\w\s]', '', text) #removes quotes that werent removed in previous step

text_array = re.split('[\s\n]', clean_text) #array of all the words, split on whitespace or newline

#count the number of occurrences of a specified word and display the count

def count_word(word):
  count = 0
  for string in text_array:
    if word.lower() == string.lower():
      count += 1
  print(f"{word} appears {count} times in the text.")

count_word('baking')

# identify the most common word

#calculate the average word length, excluding special characters and puncuation marks from the word length calculation 




#count number of paragraphs (based on empty lines between blocks of text) and display count

#count number of sentences (based on punctuation such as periods exclamation marks, and question marks) and display counts