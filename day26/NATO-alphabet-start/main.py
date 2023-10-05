

#TODO 1. Create a dictionary in this format:
import pandas



df=pandas.read_csv("./day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input=input("Please Enter a word : ")
nato_phonetics=[nato_dict[f"{letter.upper()}"] for letter in user_input]

print(nato_phonetics)


