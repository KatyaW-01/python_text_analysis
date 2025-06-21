import string
import re

file_path = 'article.txt'
  
with open(file_path, 'r') as file:
  file_content = file.read()

# the variable file_contact now contains the article.txt as a string


#count the number of occurrences of a specified word and display the count

# identify the most common word

#calculate the average word length, excluding special characters and puncuation marks from the word length calculation 

translator = str.maketrans('', '', string.punctuation)
text = file_content.translate(translator)  #removes punctuation 
clean_text = re.sub(r'[^\w\s]', '', text) #removes quotes that werent removed in previous step

split_text = re.split('[\s\n]', clean_text) #array of all the words, split on whitespace or newline



print(split_text)


#count number of paragraphs (based on empty lines between blocks of text) and display count

#count number of sentences (based on punctuation such as periods exclamation marks, and question marks) and display counts