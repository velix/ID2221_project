'''
'in_reply_to_status_id'
'contributors'
'favorited'
'in_reply_to_user_id_str'
'source'
'full_text'
'is_quote_status'
'id_str'
'in_reply_to_user_id'
'entities'
'display_text_range'
'geo'
'created_at'
'in_reply_to_status_id_str'
'truncated'
'retweet_count'
'in_reply_to_screen_name'
'id'
'lang'
'favorite_count'
'retweeted_status'
'place'
'coordinates'
'retweeted'
'user'
'''
import sqlite3
import json

class TweetAttributes:

    def __init__(self, attributes_dict):
        self._extract(attributes_dict)

    def _set_attributes(self, id, **attributes):
        self.id = id
        self.in_reply_to_status_id = attributes["in_reply_to_status_id"]
        self.in_reply_to_user_id = attributes["in_reply_to_user_id"]
        self.full_text = attributes["full_text"]
        self.retweet_count = attributes["retweet_count"]
        self.favorite_count = attributes["favorite_count"]

    def _extract(self, dictionary):
        in_reply_to_status_id = dictionary["in_reply_to_status_id"]
        in_reply_to_user_id = dictionary["in_reply_to_user_id"]
        id = dictionary["id"]
        full_text = dictionary["full_text"]
        retweet_count = dictionary["retweet_count"]
        favorite_count = dictionary["favorite_count"]

        self._set_attributes(id, in_reply_to_status_id=in_reply_to_status_id,
                             in_reply_to_user_id=in_reply_to_user_id,
                             full_text=full_text, retweet_count=retweet_count,
                             favorite_count=favorite_count)


class Tweet:

    def __init__(self, user, attributes_dict):
        self.attributes = TweetAttributes(attributes_dict)
        self.user = user

    def __str__(self):
        return f"{self.attributes.full_text}\n \
                favorites: {self.attributes.favorite_count} \
                retweets: {self.attributes.retweet_count}"

    def get_repliers(self, database):

        data = []
        with open(database, "r") as f:
            for line in f.readlines():
                data.append(json.loads(line))

        repliers = []
        for tweet_entry in data[:1000]:
            if tweet_entry["in_reply_to_status_id"] == self.attributes.id:
                repliers.append(tweet_entry["user"])

        return repliers
