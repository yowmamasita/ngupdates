from ferris import Model, ndb
from app.behaviors.unique import Unique


class Post(Model):
    class Meta:
        behaviors = (Unique,)
        uniqueness_identifier = 'objectID'

    objectID = ndb.StringProperty()
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
