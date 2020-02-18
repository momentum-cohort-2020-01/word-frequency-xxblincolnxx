import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file): #THIS IS A CALLBACK FUNCTION THAT GETS TRIGGERED BY THE IF STATEMENT BELOW
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        open_file = file.read()
        #NOW THE FILE IS A STRING WE CAN PARSE WITH OUR OTHER LOGIC
        no_punct_lowercase = clean_up_string(open_file)
        no_stop_words = remove_stop_words(STOP_WORDS, no_punct_lowercase)
        return word_freq(no_stop_words)

#--------------------------------FUNCTIONS ADAPTED FROM babysfirstpython.py STARTER FILE-----------------------------------#

def word_freq (pruned_string):
  """returns the frequency of any word used in the test string"""
  string_as_list = pruned_string.split(' ')
  string_as_list = list(dict.fromkeys(string_as_list))
  for word in string_as_list: 
    print ((word+" "+str(pruned_string.count(word))+" | ")+(" *"*(pruned_string.count(word))))

def remove_stop_words (stop_word_list, cleaned_up_string):
  """Takes List of words to remove and a string from which they will be removed. Returns 
  a string without the targetted words"""
  string_as_list = cleaned_up_string.split(" ")

  for s_word in stop_word_list:
    string_as_list = [word for word in string_as_list if word != s_word]
  
  return ' '.join(string_as_list)

def clean_up_string (raw_string):
    """removes puntuation, takes away line breaks, converts to lowercase. Takes raw string as arguement. Requires import string module"""
    fixed_string = raw_string.translate(str.maketrans('', '',string.punctuation))
    fixed_string = fixed_string.replace('\n','')
    fixed_string = fixed_string.lower()
    return fixed_string

#-------------------------------TERMINAL OPEN FILE FUNCTION-----------------------------------#

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)







