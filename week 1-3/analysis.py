import json
def unique(question):
    colors = []
    for i in x:
        num = i[question]
        color = num.lower()
        colors += [color]
    print(set(colors))
    print(f"Unique Answers: {len(set(colors))}")
f = open("answers.json", "r")
x = json.load(f)
len(x)
s = 0
for i in x:
    s += int(i["How old are you? "])
average = s/len(x)
#print(s)
print(f"The average age is {average}")
question1 = "What's your name? "
question2 = "When is your birthday? (MM/DD/YYYY) "
question3 = "How old are you? "
question4 = "Where do you live? (City, State, Country) "
question5 = "What's your favorite food? "
question6 = "What's your favorite color? "
unique(question1)
unique(question2)
unique(question3)
unique(question4)
unique(question5)
unique(question6)
f.close()
