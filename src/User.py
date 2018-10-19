import twint


class UserAttributes:

    def __init__(self, attributes_dict):
        self._extract(attributes_dict)

    def _set_attributes(self, id, **attributes):
        self.name = attributes["name"]
        self.id = id
        self.screen_name = attributes["s_name"]
        self.followers_count = attributes["fc"]

    def _extract(self, dictionary):
        name = dictionary["name"]
        screen_name = dictionary["screen_name"]
        id = dictionary["id"]
        followers_count = dictionary["followers_count"]

        self._set_attributes(id, name=name, s_name=screen_name,
                             fc=followers_count)


class User:

    def __init__(self, attributes_dict):
        self.attributes = UserAttributes(attributes_dict)

        self.followers = []

    def __str__(self):
        return f"Username: {self.attributes.name}, Id: {self.attributes.id}"

    def get_following(self):
        '''
        Get the users that this user is following
        '''

        c = twint.Config()
        c.User_id = self.attributes.id
        # The users' names are stored in the database below,
        # in the table 'following_names'
        # c.Database = "following.db"

        # Store in a JSON file
        c.Store_json = True
        c.Custom = ["username", "id"]
        c.User_full = True
        c.Output = "following.json"

        following = twint.run.Following(c)

        return following

    def get_followers(self):
        '''
        Get the users that are following this user
        '''

        c = twint.Config()
        c.User_id = self.attributes.id
        c.Database = "following.db"

        followers = twint.run.Following(c)

        return followers
