#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "52059339-XyqItMmMzqUDBskEVMzdwyw3a0tc4yOS8TPpTDuwg"
access_token_secret = "UIrtQpyt5fYDZ0hzARshz3kdi5iuK49QJntOzbX0ZV2WT"
consumer_key = "rx2cHdGs29aVXHodOZKqdQamr"
consumer_secret = "xvmt2rWuHCT5PTs8jp0xqw1yhPu4wzx39dHVd7BVUwLhmFH7G2"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    streamListener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, streamListener)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])