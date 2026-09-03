from deepmultilingualpunctuation import PunctuationModel
import queue
import time

model = PunctuationModel()

# 14, 45, 50, 114, 175, 204, 218, 294, 300, 332, 379, 395, 399, 411, 414, 425, 521, 541, 590, 607

numbers = [14, 45, 50, 114, 175]#204, 218, 294, 300, 332, 379, 395, 399, 411, 414, 425, 521, 541, 590, 607]
endpoints = queue.Queue()
block = ""
start_point = 0
text = "lorem ipsum is simply dummy text of the printing and typesetting industry lorem ipsum has been the industry's standard dummy text ever since 1966 when designers at letraset and james mosley the librarian at st bride printing library in london took a 1914 cicero translation and scrambled it to make dummy text for letraset's body type sheets it has survived not only many decades but also the leap into electronic typesetting remaining essentially unchanged it was popularised thanks to these sheets and more recently with desktop publishing software like aldus pagemaker and microsoft word including versions of lorem ipsum"
punctuated = ""


for num in numbers:
    endpoints.put(num)

while not endpoints.empty():
    end_point = endpoints.get()
    block = text[start_point:end_point]
    punct_block = model.restore_punctuation(block)
    print(punct_block)
    count = punct_block.count(".") + punct_block.count("?")
    found = 0
    index = 0
    if count >= 2:
        for letter in range(0, len(punct_block)):
            if found == count - 1:
                punctuated += punct_block[start_point:letter]
                start_point = letter
                break
            else:
                if punct_block[letter] == ".":
                    found += 1

            block = punct_block.replace("?", "").replace(".", "")
            #start_point = text.find(block, start_point) + len(block)
        #print(punctuated)