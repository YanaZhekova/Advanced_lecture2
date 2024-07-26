text = input()
char_dict = dict()
for ch in text:
    if ch not in char_dict:
        char_dict[ch]=1
    else:
        char_dict[ch] +=1

for el in sorted(char_dict.keys()):
    print(f"{el}: {char_dict[el]} time/s")