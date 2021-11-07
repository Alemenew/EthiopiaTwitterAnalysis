import unittest
import pandas as pd
import sys

sys.path.insert(1, '/Users/alex/Desktop/10_acadamy/Twitter-Data-Analysis')
from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor
from clean_tweets_dataframe import df
from clean_tweets_dataframe import CleanTweets

class TestTweetDFClean(unittest.TestCase):
    def setUp(self) -> pd.DataFrame:
        #self.CleanTweets
        self.df = TweetDfExtractor(tweet_list[:5])

if __name__ == '__main__':
	unittest.main()
