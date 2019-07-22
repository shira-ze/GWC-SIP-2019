# --- Define your functions below! ---
import time
def greetingFunction():
    print("Hi there, I am chatbot!")
def respondToUser(userAnswer):
    if(userAnswer == "good"):
        print("I'm happy to hear..... wait actually I'm not")
    elif(userAnswer == "bad"):
        print("awww...well that's too bad... deal with it?")
    else:
        greetingFunction(input("please type in 'good', or 'bad' only "))

def response2(userAnswer2):
    if(userAnswer2 == "song"):
        print("too bad, I don't know how to play music on python. You better drop and give me 20...")
    elif(userAnswer2 == "art"):
        print("too bad, I don't know how to draw art on python. You better drop and give me 20...")
    elif(userAnswer2 == "push ups"):
        print("stop being a show-off, I know you aren't even able to do one")
    else:
        response2(input("please type in 'art', 'song' or 'push ups' only "))

# --- Put your main program below! ---
def main():
    greetingFunction()


    user_input = input("how are you today?")
    respondToUser(user_input)
    time.sleep(1)
    user_input2 = input("would you rather I show you my art, play you a song or you get to do 20 push ups?")
    response2(user_input2)
    time.sleep(1)
    print("ugh, I'm bored")
    time.sleep(.5)
    print("I'm tired...")
    time.sleep(3)
    print("ok, I'm getting sick of you now, I know you didn't do those pushups... you should leave, the shows over.")
