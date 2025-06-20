file_path = 'article.txt'
  
with open(file_path, 'r') as file:
  file_content = file.read()

# the variable file_contact now contains the article.txt as a string


#count the number of occurrences of a specified word and display the count

# identify the most common word

#calculate the average word length, excluding special characters and puncuation marks from the word length calculation 
  #import string
  # translator = str.maketrans('', '', string.punctuation)
  # clean_text = file_content.translate(translator)  #this will remove all punctuation from the file so you can then just split it into words and calculate average word length 


#count number of paragraphs (based on empty lines between blocks of text) and display count

#count number of sentences (based on punctuation such as periods exclamation marks, and question marks) and display counts