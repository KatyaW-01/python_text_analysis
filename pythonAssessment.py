import string
import re

def load_article(article):
  file_path = article
  with open(file_path, 'r') as file:
    file_content = file.read() #article.txt as a string, stored in file_content
  return file_content

def clean_article():
  file = load_article('article.txt')
  clean_text = re.sub(r'[^\w\s]','',file)
  return clean_text

def split_article():
  clean_text = clean_article()
  text_array = re.split('[\s\n]', clean_text) #array of all the words, split on whitespace or newline
  return text_array

def count_specific_word(word):
  count = 0
  clean_word = word.strip().lower() #removes leading and trailing whitespaces and makes lowercase
  text_array = split_article()
  for string in text_array:
    if clean_word == string.lower():
      count += 1
  print(f"'{clean_word}' appears {count} times in the text.")

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
  remove_inc = text.replace('Inc.','Inc') #remove period after Inc. so it doesnt mess up splitting string by .
  remove_dr = remove_inc.replace('Dr.', 'Dr') #Remove period after Dr.
  replaced_text = re.sub(r'[“”"]', '', remove_dr) #remove quotations
  sentences = re.split('[.!?]', replaced_text) #split at . ! ?
  count = 0
  for sentence in sentences:
    if len(sentence) > 1:
      count += 1
    #excludes elements of just '\n\
  print(f"There are {count} sentences in the text")


#function calls
while True:
  try:
    word = input("Enter a word you want to count in the text: ")
    if not word:
      raise ValueError("Input cannot be empty.")
    if word == ' ':
      raise ValueError("Input cannot be empty")
    if word.isdigit():
      raise ValueError("Input cannot be a number, please enter a word.")
    count_specific_word(word)
    break
  except ValueError as e:
    print(f"Error: {e}")

identify_most_common_word(split_article())
calculate_average_word_length(split_article())
count_paragraphs(clean_article())
count_sentences(load_article('article.txt'))