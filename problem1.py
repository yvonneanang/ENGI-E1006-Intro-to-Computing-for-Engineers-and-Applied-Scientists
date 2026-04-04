#collaborated with xz2782, jd3549, and another girl whose uni i have misplaced
#submitted by Yvonne Naa Ardua Anang UNI: yna2103
from collections import defaultdict
import string

def count_ngrams(file_name, n): 
     read_file = open(file_name, "r")
     long_list_of_words = []
     ngram_to_count = {}
     ngram_list = []
     a = 0
     for line in read_file:
         short_list_of_words = line.strip().split()
         for word in short_list_of_words:
             new_word = word.strip(string.punctuation).lower()
             long_list_of_words.append(new_word)
             
     for word in long_list_of_words:
         if n == 1:
             ngram_list.append(tuple(word))
         else:
             while a < len(long_list_of_words) and (a+n) != (len(long_list_of_words) + 1):
                 one_ngram = tuple(long_list_of_words[a: (a + n)])
                 ngram_list.append(one_ngram)
                 a += 1
                 
     for ngram in ngram_list:
         if ngram[:len(ngram) + 1] in ngram_to_count:
             ngram_to_count[ngram] += 1
         else:
             ngram_to_count[ngram] = 1
     return ngram_to_count
             
     """
     This function reads an input file and returns a dictionary of n-gram counts.  
     file_name is a string, n is an integer. 
     The result dictionary maps n-grams to their frequency (i.e. the count of 
     how often that n-gram appears). Each n-gram key is a tuple and the count is
     an int.
     """


def single_occurences(ngram_count_dict):
    list_of_ngrams_single_occurences = []
    for ngram in ngram_count_dict:
        if ngram_count_dict[ngram] == 1:
            list_of_ngrams_single_occurences.append(ngram)
    return list_of_ngrams_single_occurences
    """
    This functions takes in a dictionary (in the format produces by 
    count_ngrams) and returns a list of all ngrans with only 1 occurence.
    That is, this function should return a list of all n-grams with a count
    of 1. 
    """


def most_frequent(ngram_count_dict, num): 
    most_frequent_occurence_list = []
    unsorted_frequency_ngram_list = []
    sorted_frequency_ngram_list = []
    frequency_list = []
    count_ngram = []
    for ngram, count in ngram_count_dict.items():
        count_ngram.append(count)
        count_ngram.append(ngram)
        count_ngram_tuple = tuple(count_ngram)
        unsorted_frequency_ngram_list.append(count_ngram_tuple)
        count_ngram =[]
    for count_ngram_tuple in unsorted_frequency_ngram_list:
        frequency_list.append(count_ngram_tuple[0])
    frequency_list.sort()
    for number in range(len(frequency_list), 0, -1):
        for count_ngram_tuple in unsorted_frequency_ngram_list:
            if count_ngram_tuple[0] == number:
                sorted_frequency_ngram_list.append(count_ngram_tuple)
    for i in range(num):
        most_frequent_occurence_list.append(sorted_frequency_ngram_list[i][1])
    return most_frequent_occurence_list
    
    """
    This function takes in two parameters: 
        ngram_count_dict is a dictionary of ngram counts. 
        num denotes the number of n-grams to return.       
    This function returns a list of the num n-grams with the highest
    occurence in the file. For example if num=10, the method should 
    return the 10 most frequent ngrams in a list. 
    """

def main():
    filename = "alice.txt"
    n = 2
    most_frequent_k = 5

    ngram_counts = count_ngrams(filename, n)

    print('{}-grams that occur only once:'.format(n))
    print(single_occurences(ngram_counts))

    print('{} most frequent {}-grams:'.format(most_frequent_k, n))
    print(most_frequent(ngram_counts, most_frequent_k))

if __name__ == "__main__":
    main()
