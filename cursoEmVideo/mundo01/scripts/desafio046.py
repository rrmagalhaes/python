from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
#print('💥💥💥💥💥💥💥💥💥💥')
print(emoji.emojize(':boom:', use_aliases=True) * 10)