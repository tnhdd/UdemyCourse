import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(new_dict)
words = input("Type a word: ").upper()
result = [new_dict[letter] for letter in words]
print(result)
