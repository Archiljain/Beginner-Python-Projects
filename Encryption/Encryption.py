import random
import string
def generate_random_string(length):
   characters = string.ascii_lowercase + string.digits
   return ''.join(random.choice(characters) for i in range(length))
coding = input("1 for coding or 0 for decoding ")
st =input("Enter message :")
words = st.split(" ")
coding = True if coding == "1" else False
if(coding):
   nwords = []
   for word in words:
    if(len(word)>= 3):
       r1 = generate_random_string(3)
       r2 = generate_random_string(3)
       stnew = r1 + word[1:] + word[0] + r2
       nwords.append(stnew)
    else:
       nwords.append(word[::-1])
   print(" ".join(nwords))
else:
 nwords = []
 for word in words:
    if(len(word)>= 3):
       stnew = word[3:-3]
       stnew = stnew[-1:] + stnew[:-1]
       nwords.append(stnew)
    else:
       nwords.append(word[::-1])
 print(" ".join(nwords))