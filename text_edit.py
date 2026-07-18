import difflib as dl

def edit(first, second):
    length = len(first)
    start = int(len(second) / 2)
    cut = first[start:length]

    accuracy = dl.SequenceMatcher(None, cut, second[0:int(len(second) / 2)]).ratio() * 100
    index = -1

    print(accuracy)

    print(f"1. {first}")
    print(f"c. {cut}")
    print(f"2. {second}")

    if len(first) <= len(second) * 2:
        print("a")
        for letter in range(0, len(first) - 5):
            if first[letter:letter+5] == second[0:5]:
                index = letter
        
        if index < 0:
            print("No match")
            return first + second
        else:
            final = first[0:index] + second
            return(final)
    else:
        print("b")
        for letter in range(0, len(cut) - 5):
            if cut[letter:letter+5] == second[0:5]:
                index = letter

        if index < 0:
            print("No match")
            return first + second
        else:
            final = first[0:start] + cut[0:index] + second
            return(final)

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

