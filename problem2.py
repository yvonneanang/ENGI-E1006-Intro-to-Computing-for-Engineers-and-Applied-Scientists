#submitted by Yvonne Naa Ardua Anang (uni:yna2103)
#collaborated with Joseph Duodu(uni: jd3519)
def print_box(s):
    if "\\n" in s:
        boxed_list = s.split("\\n")
        len_of_longest_word = 0
        for i in boxed_list:
            if len(i) > len_of_longest_word:
                len_of_longest_word = len(i)
        
        length_of_box = (len_of_longest_word + 4) * "*"
        print (length_of_box)
        for word in boxed_list:
            length_of_space = (((len_of_longest_word + 4) - len(word))//2)-1
            if len(word) % 2 == 0:
                s_new = "*" + (" " * length_of_space ) + word + (" " * length_of_space ) + "*"
            elif len(word)%2 != 0:
                s_new = "*" + (" " * length_of_space ) + word + (" " * (length_of_space+1) ) + "*"
            print (s_new)
        print (length_of_box)
    else:
        length_of_box = (len(s)+4) * "*"
        s_new = "* " + s + " *"
    
        print (length_of_box)
        print (s_new)
        print (length_of_box)
    return ""

s = input("Please type a string:>>>")
print(print_box(s))