import json
from Tweet import Tweet
from User import User

if __name__ == "__main__":
    file = "/home/velisarios/Downloads/J2o/tweets.json"

    data = []
    with open(file, "r") as f:
        for line in f.readlines():
            data.append(json.loads(line))

    for tweet_entry in data[:1000]:
        user = User(tweet_entry["user"])
        tweet = Tweet(user, tweet_entry)

        print(user)
        print(tweet)
        # following = user.get_following()
        # followers = user.get_followers()
        # print()
        repliers = tweet.get_repliers(file)
        print(len(repliers))
        print(repliers)
        print()