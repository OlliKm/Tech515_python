#the dictionary
story1 =  {"start": "A mouse took a stroll through the deep dark wood",
           "middle": "a fox/owl/snake saw the mouse and wanted to eat it",
           "end": "the mouse tricked the fox/owl/snake and went on to scare a gruffalo"}


chapter = story1.keys() # crating a value for out keys
#for every chapter within story1.keys() print itself which is the key of our dictionary
print("the keys in the story")
print(chapter)
print(type(chapter))
print("\n")
for chapter in story1.keys():
    print(chapter)
#-----------------------------------------------
print(" ")

values = story1.values() # values is the same as story1.values
for values in story1.values():#every mention of itself, print its values
    print(values)

#Print the individual values using the keys
print("\n")
print(story1["start"])
print("\n")
print(story1["middle"])
print("\n")
print(story1["end"])


story1["character"] = "The Cunning Mouse" #appending the character into dict
print("\n")
# end story
story1["credits"] = "I hope you enjoyed the short little story" # appending credits
print(f"The end ",story1["credits"], "signed by",story1["character"]) #printing credits and character
