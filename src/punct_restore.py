from deepmultilingualpunctuation import PunctuationModel

model = PunctuationModel()
text = "does this program work let us find out"
result = model.restore_punctuation(text)
print(result)