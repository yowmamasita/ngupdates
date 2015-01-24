from ferris import Model, ndb


class Post(Model):
    title = ndb.StringProperty()
    url = ndb.StringProperty()

    @classmethod
    def create(cls, params):
        item = cls(**params)
        item.put()
        return item

    def update(self, params):
        self.populate(**params)
        self.put()

    def delete(self):
        ndb.delete_multi(self.__class__.query(ancestor=self.key).iter(keys_only=True))

    @classmethod
    def list(cls):
        return cls.query()
