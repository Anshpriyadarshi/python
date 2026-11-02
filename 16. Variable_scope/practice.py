text = input("Enter the string:~")
char = {}
for ch in text:
    if ch.isalpha(): 
        if ch in char:
            char[ch] += 1  
        else:
            char[ch] = 1  
for ch, count in char.items():
    print(f"{ch}{count}", end=' ')  

