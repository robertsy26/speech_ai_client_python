import difflib as dl

def edit(first, second):
    length = len(first)
    start = length - len(second)
    cut = first[start:length]

    accuracy = dl.SequenceMatcher(None, cut, second[0:int(len(second) / 2)]).ratio() * 100

    #print(first)
    #print(cut)
    #print(second)

    index = -1

    for letter in range(0, len(cut) - 5):
        if cut[letter:letter+5] == second[0:5]:
            index = letter

    if index < 0:
        print("No match")
    else:
        final = first[0:start] + cut[0:index] + second
        return(final)

    print(f"{accuracy:.2f}")

'''
string1 = " This is the end of the world. What? is? your. recording level?"
string2 = " What is your recording level DBFS? rover"
string3 = " Recording level DBFS. rover is over"
main = "this is the end of the world what is your recording level dbfs rover"

string1n = string1.replace("?", "").replace(".", "").lower().lstrip()
string2n = string2.replace("?", "").replace(".", "").lower().lstrip()
string3n = string3.replace("?", "").replace(".", "").lower().lstrip()

edit(main, string3n)
'''

