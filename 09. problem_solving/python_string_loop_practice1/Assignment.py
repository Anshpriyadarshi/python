#Question - 1
number = input("Enter the string:~")

if "420" in number:
    print("caught")
else:
    print("Escaped")

#Question - 2
def decompress_String(s):
    result = []
    for i in range(0, len(s), 2):
        letter = s[i]
        count = int(s[i + 1])
        result.append(letter * counrt)
    return ' '.join(result)
input_string = input("Enter the compressed string:~")
output_string = decompress_string(input_string)
print(output_string)

#Question - 3 