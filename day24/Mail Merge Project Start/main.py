#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

STARTING_LETTER="./day24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
NAMES="./day24/Mail Merge Project Start/Input/Names/invited_names.txt"
with open(NAMES) as file:
    names=file.readlines()


names=[x.strip() for x in names ]

for name in names:
    with open(STARTING_LETTER) as file:
        orginal_letter=file.read()
    final_letter=orginal_letter.replace("[name]",name)
    with open(f"./day24/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(final_letter)
        
