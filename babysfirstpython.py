# beers = ['lager', 'stout', 'IPA', 'pale ale', 'porter', 'blonde', 'pilzner']

# for beer in beers:
#   print(beer+" length is " +str(len(beer)))

# print(string_step12.count("the"))
# print(string_step12.count("semantics"))

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

test_string = ("Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane.")
#--------------------------------TASKS--------------------------------------
# remove punctuation ****CHECK
# normalize all words to lowercase ****CHECK
# remove "stop words" -- words used so frequently they are ignored
# go through the file word by word and keep a count of how often each word is used
#-------------------------------FUNCTIONS-----------------------------------
import string

def fix_string (input_string):
  """Removes punctuation from a string and makes lowercase"""
  # changed_string = input_string.replace(".", "")
  # changed_string = changed_string.replace(",", "")
  # changed_string = changed_string.replace("!", "")
  # changed_string = changed_string.replace("=", "")
  # changed_string = changed_string.replace("?", "")
  # changed_string = changed_string.replace(":", "")
  # changed_string = changed_string.replace(";", "")
  # changed_string = changed_string.replace("-", "")
  # changed_string = changed_string.replace("\'", "")
  # changed_string = changed_string.replace("\"", "")
  # changed_string = changed_string.replace("/", "")
  # changed_string = changed_string.replace("}", "")
  # changed_string = changed_string.replace("*", "")
  # changed_string = changed_string.replace("+", "")
  # changed_string = changed_string.replace("#", "")
  # changed_string = changed_string.replace("@", "")
  # changed_string = changed_string.replace("(", "")
  # changed_string = changed_string.replace(")", "")
  # return changed_string
  fixed_string = input_string.translate(str.maketrans('', '',string.punctuation)) #removed punctuation... does same as comments
  fixed_string = fixed_string.lower()
  return fixed_string

def remove_stop_words (stop_word_list, cleaned_up_string):
  """attempt 1 --- I sift through the words list and
  replace each word with an empty quote. Problem is that the function
  doesn't make a distinction between words and a non-word combo of characters.
  So it's removing "it" from "spit"... returning "sp". New approach. UPDATE - Looks like I could have added spaces to the arguement of "replace" and it would have worked: string.replace(" "+it+" ", " ")... but I like the way attempt 2 came out"""

  # deboned_string = cleaned_up_string
  # for word in stop_word_list:
  #   deboned_string = deboned_string.replace(word, "")
  
  """attempt 2 --- I'm going to turn the string to a list, parse the list and 
  check it against the list of junk words, remove the junk words, then join the 
  resulting list as a new string."""
  string_as_list = cleaned_up_string.split(" ")

  for s_word in stop_word_list:
    string_as_list = [word for word in string_as_list if word != s_word]
  
  return ' '.join(string_as_list)


string_step12 = fix_string(test_string)
string_steps123 = remove_stop_words(STOP_WORDS, string_step12)

# def show_count_stop_words (fixed_string, stop_word_list):
#   """I seem to have misunderstood the question... I'm not supposed to count the number of stopwords. But here's a function that does that:"""
#   for s_word in stop_word_list:
#     print(s_word+" |"+str(fixed_string.count(" "+s_word+" "))+(" *"*(fixed_string.count(" "+s_word+" "))))

def word_freq(pruned_string):
  """returns the frequency of any word used in the test string"""
  string_as_list = pruned_string.split(' ')
  string_as_list = list(dict.fromkeys(string_as_list))
  for word in string_as_list: 
    print ((word+" "+str(pruned_string.count(word))+" | ")+(" *"*(pruned_string.count(word))))

# print(string_step12.count("the"))
# print(string_step12.count("semantics"))

# print(string_step12)
# print(show_count_stop_words(string_step12, STOP_WORDS))
print(word_freq(string_steps123))

