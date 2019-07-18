'''
In this program, we print out all the text data from our twitter JSON file.

Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# def numOfLetter(tw, letter):
# 	count = 0
# 	for l in tw:
# 		if l == letter or l.lower() == letter:
# 			#print(l)
# 			count += 1
# 	return count
#
#
#
# # Next we want to open the JSON file. We tag this file as
# # "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")
#
# # We use the JSON library to get data from the file as JSON data. (load function only exists bc json library was imported)
tweetData = json.load(tweetFile)
tweetFile.close()
# print(type(tweetData))
# print(type(tweetData[0]))
# # list(newdict.keys())
# print(list(tweetData[0].keys()))
# #this (above) shows the te name of all the keys in the list's index 0, such as ['created_at', 'favorite_count', 'hashtags', 'id', 'id_str', 'lang', 'retweet_count', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']
# #to see the value of one of those keys:
# # print(tweetData[0]["created_at"])
#
#
# #HERE (BELOW) IS THE CODE TO FIND THE AVERAGE
# sum = 0
# num = 0 #the amount of tweets total that have favorites- the total when divide sum by total
# for i in range(len(tweetData)):
# 	# print(i)
# 	tweet = tweetData[i]
# 	if "favorite_count" not in tweet:
# 		# print("missing")
# 		print(len(tweet.keys()))
# 		print(tweet.keys())
# 	else:
# 		print("this is WORKINGSFGSFDGDS")
# 		num += 1
# 		sum += tweetData[i]["favorite_count"]
#
# average = sum/num
# print("here is avg!!!!!!!!!!")
# print(average)
#
#
tweetList = []
for i in range(len(tweetData)):
	tweetList.append(tweetData [i]["text"])
# print(tweetList)
#
# tweetID = []
# for i in range(len(tweetData)):
# 	tweetList.append(tweetData [i]["id"])
# print(type(tweetID))
#
#
#

polarityList = []
for item in tweetList:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	polarityList.append(polar1)
# print(polarityList)
#
# ***THERE SEEMS TO BE SOME ISSUES HERE***
# tweetpol = {}
# leest = []
# for i in range(0,len(tweetData)):
# 	dictionaree = {}
# 	dictionaree ["tid"] = tweetData[i][id]
# 	dictionaree ["polarity"] = polarity_list[i]
# 	dictionaree ["tweet"] = texts [i]
# 	leest.append(dictionaree)
# print(leest)

#turn all tweets into one long string by taking the tweets in the tweet list and iterat thru it
tweetstring = " "
for tweet in tweetList:
	tweet = tweet + " " #this reassigns tweet to be tweet plus a space
	tweetstring += tweet
# print(tweetstring)
wordcloud = WordCloud(). generate(tweetstring)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.savefig("shira'schart.png")

# new Thing
# tb = TextBlob("you are compsists") #this returns tb, a "text blob object" which you could do a  lot of things to like print the polarity...



#tweet data is the var name for what us now storing all the twiiter data from JSON
# We can close the file now that we have locally stored the data.
#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
