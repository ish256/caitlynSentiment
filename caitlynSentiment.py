import twitter
import oauthDance
import pprint
import pandas as pd
import readSentimentListFile as sentList
import classifySentimentFile as sentClass


#This script loads up popular twitter data over a given time span and conducts 
#sentiment analysis on the collected data

t = oauthDance.login() #login to twitter api 

#search query constructed to collect popular tweets over a day using tweet unique ids ( first day )
CallmeCaitlyn = t.search.tweets(q="CallmeCaitlyn popular since_id:605406096824647681 max_id:605627076637564928")
#construct data frame to contain data 
attribute_names = CallmeCaitlyn["statuses"][1].keys()

our_df = pd.DataFrame( columns = attribute_names )


our_df = our_df.append( CallmeCaitlyn["statuses"]) #might have to change the name to reflect the date!

# #search query constructed to collect popular tweets over a day using tweet unique ids ( second day )
# CallmeCaitlyn = t.search.tweets(q="CallmeCaitlyn popular since_id:605627076637564928 max_id:605949822198259713")
# our_df = our_df.append( CallmeCaitlyn )

# #search query constructed to collect popular tweets over a day using tweet unique ids ( third day )
# CallmeCaitlyn = t.search.tweets(q="CallmeCaitlyn popular since_id:605949822198259713 max_id:606309690872578049")
# our_df = our_df.append( CallmeCaitlyn )


############################code for tokenization and classifying tweets in a given day##################

# We load in the list of words and their log probabilities
happy_log_probs, sad_log_probs = sentList.readSentimentList('twitter_sentiment_list.csv')

#classificationLabels = ["negative" , "positive"]
#allTweetsInADayClassification =  pd.DataFrame(columns=classificationLabels)

for i in range(0,our_df.shape[0]):	
    # Here we have tweets which we have already tokenized (turned into an array of words)
    curTweet = our_df['text'][i].split()
    # Calculate the probabilities that the tweets are happy or sad
    happy_prob, tweet1_sad_prob = sentClass.classifySentiment(curTweet, happy_log_probs, sad_log_probs)
    print "The probability that tweet1 (", curTweet, ") is happy is ", happy_prob, "and the probability that it is sad is ", tweet1_sad_prob
	#allTweetsInADay.extend( our_df['text'][i].split() )
