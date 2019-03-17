import random

ifile=open('hangman.txt','r')
data=ifile.readlines()
rword=data[random.randint(0,len(data))].strip("\n").lower()
maut=5
vowel=['a','e','i','o','u']
update=[0 for i in range(len(rword))]

def st(word):
    # word is a list. Function returns string of word.
    return "".join(word)


print("\n\t\t\tWelcome to Hangman!")
print("\n\t\t  Guess the movie:\t",end="")
# Printing the question...!

for l in range(len(rword)):
    if rword[l] in vowel:
        update[l]=rword[l]
    elif rword[l]==" ":
        update[l]="  "
    else:
        update[l]="_ "
print(st(update))


def display(guess,rword,update):
    for l in range(0,len(rword)):
        if rword[l]==guess:
            update[l]=guess
    return(update)
      

# Aslii Game here...!

while maut!=0 and st(update).split()!=rword.split():
    guess=input("\n\t\t  Guess a letter: \t").lower()
    if guess in rword:
        if guess not in update:
            update=(display(guess,rword,update))
            print("\t\t",st(update))
        else:
            print("\t\tLetter already present! Try another one")
    else:
        maut-=1
        print("\t\t",5-maut,"strikes down! ",maut,"strikes left. :D")
else:
    if maut!=0:
        print("\t\tYou win! :D")
    else:
        print("\n\t\tYou lose! ;_;\n")
        print("\t\tThe movie was:",rword.capitalize())
