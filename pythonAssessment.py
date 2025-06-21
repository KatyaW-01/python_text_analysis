import string
import re

file_path = 'article.txt'
  
with open(file_path, 'r') as file:
  file_content = file.read() #article.txt as a string, stored in file_content

translator = str.maketrans('', '', string.punctuation)
text = file_content.translate(translator)  #removes punctuation 
clean_text = re.sub(r'[^\w\s]', '', text) #removes quotes that werent removed in previous step

text_array = re.split('[\s\n]', clean_text) #array of all the words, split on whitespace or newline

def count_word(word): #refactor to use user input here
  count = 0
  for string in text_array:
    if word.lower() == string.lower():
      count += 1
  print(f"{word} appears {count} times in the text.")

count_word('baking')

# identify the most common word



#calculate the average word length, excluding special characters and puncuation marks from the word length calculation 

def average_word_length():
  word_length = []
  for string in text_array:
    word_length.append(len(string))

  total = 0
  for num in word_length:
    total += num
  
  average_word_length = round((total/len(word_length)),2)
  print(F"The average word length is {average_word_length}.")



average_word_length()




#count number of paragraphs (based on empty lines between blocks of text) and display count
def paragraph_count():
  paragraphs = re.split('[\n]', clean_text) #split text at newlines
  count = 0
  for paragraph in paragraphs:
    if len(paragraph) > 0: #doesnt count empty strings for double newlines
      count += 1

  print(f"There are {count} paragraphs in the text")

paragraph_count()

#count number of sentences (based on punctuation such as periods exclamation marks, and question marks) and display counts