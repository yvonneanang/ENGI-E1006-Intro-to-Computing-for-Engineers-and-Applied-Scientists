#submitted by Yvonne Naa Ardua Anang (uni:yna2103)
#collaborated with Joseph Duodu(uni: jd3519)
#part 1
def find(s, substring):
    if substring in s:
        for x in range(len(s)):
            if s[x] == substring[0]:
                return x
                break
    else:
        return -1

#part 2
def find_multi(s, substring):
    list_of_indices = []
    if substring in s:
        for x in range(len(s)):
            if substring == s[x:x + len(substring)]:
                list_of_indices.append(x)
        return list_of_indices
            
    else:
        return []

            
            