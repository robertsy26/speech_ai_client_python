from difflib import SequenceMatcher

string1 = " This is the end of the world. What? is? your. recording level?"
string2 = " What is your recording level DBFS? rover"
string3 = " Recording level DBFS. rover is over"
main = "what is your recording level"

string1n = string1.replace("?", "").replace(".", "").lower().lstrip()
string2n = string2.replace("?", "").replace(".", "").lower().lstrip()
string3n = string3.replace("?", "").replace(".", "").lower().lstrip()

length = len(string1n)
start = length - int(len(string3n) / 2)
cut = string1n[start:length]

accuracy = SequenceMatcher(None, cut, string3n[0:int(len(string3n) / 2)]).ratio() * 100

print(f"{accuracy:.2f}")