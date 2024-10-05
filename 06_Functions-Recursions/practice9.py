def remove(l:list[str],word:str):
    n=[]
    for item in l:
        if item==word:
            continue
        elif item!=word:
            n.append(item.strip(word))
    return n
    

def main():
    l=[]
    n=""
    while n!="exit":
        n=input("Enter string: ")
        if n=="exit":
            break
        l.append(n)
    print(l)
    word=input("Enter word to remove: ")
    l=remove(l,word)
    print(l)
    
main()
        
        