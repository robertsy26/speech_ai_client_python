from deepmultilingualpunctuation import PunctuationModel

model = PunctuationModel()
text = "does this"
result = model.restore_punctuation(text)
print(result)

text = "program work"
result = model.restore_punctuation(text)
print(result)

text = " us find out"
result = model.restore_punctuation(text)
print(result)

text = "does this program work let"
result = model.restore_punctuation(text)
print(result)

text = "does this program work let us find out"
result = model.restore_punctuation(text)
print(result)

text = "can i have some too"
result = model.restore_punctuation(text)
print(result)

text = "my name is mr l my name is dr who and he is a doctor"
result = model.restore_punctuation(text)
print(result)