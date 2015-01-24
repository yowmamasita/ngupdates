from ferris import Model, ndb


class Post(Model):
    title = ndb.StringProperty()
    url = ndb.StringProperty()
