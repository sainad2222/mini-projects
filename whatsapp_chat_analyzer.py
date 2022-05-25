# export whatsapp chat as chat.txt and remove first line from the file
from collections import defaultdict
import re
import emoji

f = open('chat.txt','r')
lines = f.readlines()
f.close()

output = ''
all_messages = []
curMessage = ''
for line in lines:
    if re.match(re.compile(r'^(\d+\/\d+\/\d+)\w+',re.MULTILINE),line):
        all_messages.append(curMessage)
        curMessage = line
    else:
        curMessage += line
all_messages.append(curMessage)
print("Total messages:",len(all_messages))

# filtering for names
one_name = None
for i in range(20):
    try:
        name = all_messages[i].split('-')[1].split(':')[0]
    except:
        continue
    if one_name == None:
        one_name = name
    else:
        two_name = name
        break
one_name = one_name.strip()
two_name = two_name.strip()

two_emojis = defaultdict(int)
two_cnt,one_cnt = 0,0
one_emojis = defaultdict(int)
one_media_cnt,two_media_cnt = 0,0
for message in all_messages:
    isMine = message.count(one_name) > 0
    if isMine:
        one_cnt += 1
    else:
        two_cnt += 1
    if message.count("<Media omitted>") == 0:
        if isMine:
            one_media_cnt += 1
        else:
            two_media_cnt += 1
    for char in message:
        if char in emoji.EMOJI_DATA:
            if isMine:
                one_emojis[char] += 1
            else:
                two_emojis[char] += 1
one_emojis = {k:v for k,v in sorted(one_emojis.items(),reverse = True,key = lambda item: item[1])}
two_emojis = {k:v for k,v in sorted(two_emojis.items(),reverse = True,key = lambda item: item[1])}

print(one_name)
print("Count:",one_cnt)
print("Without media Count:",one_media_cnt)
print("No. of different emojis",len(one_emojis))
print("Emojis count:")
for emj in one_emojis:
    print(emj+'\t'+str(one_emojis[emj]))

print()
print()

print(two_name)
print("Count:",two_cnt)
print("Without media Count:",two_media_cnt)
print("No. of different emojis",len(two_emojis))
print("Emojis count:")
for emj in two_emojis:
    print(emj+'\t'+str(two_emojis[emj]))
