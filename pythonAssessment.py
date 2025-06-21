import string
import re

def load_article():
  file_path = 'article.txt'
  with open(file_path, 'r') as file:
    file_content = file.read() #article.txt as a string, stored in file_content
  return file_content

def clean_article():
  file = load_article()
  translator = str.maketrans('', '', string.punctuation)
  text = file.translate(translator)  #removes punctuation 
  clean_text = re.sub(r'[^\w\s]', '', text) #removes quotes that werent removed in previous step
  return clean_text

def split_article():
  clean_text = clean_article()
  text_array = re.split('[\s\n]', clean_text) #array of all the words, split on whitespace or newline
  return text_array

def count_specific_word(word): #refactor to use user input here
  count = 0
  clean_word = word.strip().lower() #removes leading and trailing whitespaces and makes lowercase
  text_array = split_article()
  for string in text_array:
    if clean_word == string.lower():
      count += 1
  print(f"{clean_word} appears {count} times in the text.")

def identify_most_common_word(text):
  word_dictionary = {}
  for word in text:
    lowercase_word = word.lower() #lowercase so no duplicates of words
    if lowercase_word not in word_dictionary:
      word_dictionary[lowercase_word] = 0
    word_dictionary[lowercase_word] += 1
  maximum_value = max(word_dictionary,key=word_dictionary.get)
  print(f"The most common word in the text is '{maximum_value}'.")

def calculate_average_word_length(text):
  word_length = []
  for string in text:
    word_length.append(len(string))
  total = 0
  for num in word_length:
    total += num
  average_word_length = round((total/len(word_length)),2)
  print(F"The average word length is {average_word_length}.")

def count_paragraphs(text):
  paragraphs = re.split('[\n]', text) #split text at newlines
  count = 0
  for paragraph in paragraphs:
    if len(paragraph) > 0: #doesnt count empty strings
      count += 1
  print(f"There are {count} paragraphs in the text")

def count_sentences(text):
  new_text = text.replace('Inc.','Inc') #remove period after Inc. so it doesnt mess up splitting string by .
  #remove Dr.
  replaced_text = re.sub(r'[“”"]', '', new_text) #remove quotations
  sentences = re.split('[.!?]', replaced_text)
  count = len(sentences)
  print(f"There are {count} sentences in the text")


#function calls
try:
  word = input("Enter a word you want to count in the text: ")
  count_specific_word(word)
  #add validations for input 
except ValueError as e:
  print(f"Error:{e}")
identify_most_common_word(split_article())
calculate_average_word_length(split_article())
count_paragraphs(clean_article())
count_sentences(load_article())