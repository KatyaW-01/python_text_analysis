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
  clean_word = word.strip().lower() #removes leading and trailing whitespaces and makes lowercase
  print("clean word:",clean_word)
  for string in text_array:
    if clean_word == string.lower():
      count += 1
  print(f"{clean_word} appears {count} times in the text.")


word = input("Enter a word you want to count in the text: ")

count_word(word)

# identify the most common word




def average_word_length(text):
  word_length = []
  for string in text:
    word_length.append(len(string))

  total = 0
  for num in word_length:
    total += num
  
  average_word_length = round((total/len(word_length)),2)
  print(F"The average word length is {average_word_length}.")

average_word_length(text_array)

def paragraph_count(text):
  paragraphs = re.split('[\n]', text) #split text at newlines
  count = 0
  for paragraph in paragraphs:
    if len(paragraph) > 0: #doesnt count empty strings
      count += 1

  print(f"There are {count} paragraphs in the text")

paragraph_count(clean_text)

def count_sentences(text):
  #replace Inc. with Inc
  #remove quotes 
  #split at .!?
  #return length of that array
  count = 0
  print(f"There are {count} sentences in the text")
