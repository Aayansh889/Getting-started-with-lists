def match(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print(f"List of words with same first letter and last letter is{list}")
    return ctr

counter=match(["abc","cfc","xyz","aba","1221"])
print("Number of words having same first letter and last letter is:",counter)