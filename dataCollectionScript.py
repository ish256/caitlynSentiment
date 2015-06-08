import twitter
import oauthDance
import pandas as pd
import json

#This script collects twitter data from the twitter api and saves them
#into a json file.

###############CallmeCaitlyn Hashtag Query#################

t = oauthDance.login() #login to twitter api 

startindex = 605406096824647681 
endindex = 606309690872578049

CallmeCaitlyn = t.search.tweets(q="CallmeCaitlyn since_id:606309690872578049 max_id:606315714832897584")
attribute_names = CallmeCaitlyn["statuses"][1].keys()
our_df = pd.DataFrame(columns = attribute_names)
our_df = our_df.append( CallmeCaitlyn["statuses"]) 

for x in range(startindex, endindex, 6023960319535):
	CallmeCaitlyn = t.search.tweets(q="CallmeCaitlyn since_id:"+str(x)+" max_id:"+str(x+6023960319535))
	our_df = our_df.append(CallmeCaitlyn["statuses"]) 

tweetList = []
with open( "CallmeCaitlyn.json", 'w') as textFile:  #remember to change file name to correct date!!
	for tweet in CallmeCaitlyn["statuses"]:
		tweetList.append(tweet)
	json.dump(tweetList, textFile)


###############BruceJenner Hashtag Query#################

Bruce = t.search.tweets(q="BruceJenner since_id:606309690872578049 max_id:606315714832897584")
attribute_names = Bruce["statuses"][1].keys()
our_df2 = pd.DataFrame(columns = attribute_names)
our_df2 = our_df2.append( Bruce["statuses"]) 

for x in range(startindex, endindex, 6023960319535):
	Bruce = t.search.tweets(q="BruceJenner  since_id:"+str(x)+" max_id:"+str(x+6023960319535))
	our_df2 = our_df2.append(Bruce["statuses"]) 

tweetList = []
with open( "Bruce.json", 'w') as textFile:  #remember to change file name to correct date!!
	for tweet in Bruce["statuses"]:
		tweetList.append(tweet)
	json.dump(tweetList, textFile)

###############CaitlynJenner Hashtag Query#################

Caitlyn = t.search.tweets(q="CaitlynJenner since_id:606309690872578049 max_id:606315714832897584")
attribute_names = Caitlyn["statuses"][1].keys()
our_df3 = pd.DataFrame(columns = attribute_names)
our_df3 = our_df3.append( Caitlyn["statuses"]) 

for x in range(startindex, endindex, 6023960319535):
	Caitlyn = t.search.tweets(q="CaitlynJenner since_id:"+str(x)+" max_id:"+str(x+6023960319535))
	our_df3 = our_df3.append(Caitlyn["statuses"]) 

tweetList = []
with open( "Caitlyn.json", 'w') as textFile:  #remember to change file name to correct date!!
	for tweet in Caitlyn["statuses"]:
		tweetList.append(tweet)
	json.dump(tweetList, textFile)
