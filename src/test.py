import difflib as dl

first = "the quick brown fox jumps over the lazy dog "
second = "the brown fox jumps over the lazy dog "
accuracy = dl.SequenceMatcher(None, first, second).ratio() * 100

print(accuracy)