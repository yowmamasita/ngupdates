from google.appengine.ext import ndb
from ferris.core.ndb import Behavior


class Unique(Behavior):
    """
    Type my docstring here
    """
    def _get_id(self):
        if hasattr(self.Model.Meta, 'uniqueness_identifier'):
            return self.Model.Meta.uniqueness_identifier
        else:
            return 'name'

    def before_put(self, instance):
        key = instance.key.id()
        unique_prop = getattr(instance, self._get_id()).replace(' ', '_').lower()
        unique_key = ndb.Key(self.Model, unique_prop)
        # new entity
        if not key:
            if unique_key.get():
                raise UniqueError("Not unique")
            else:
                instance.key = unique_key
        # updating instance, key exists
        else:
            # change in value of unique prop
            if key != unique_prop:
                # check if it already exists
                if unique_key.get():
                    raise UniqueError("Not unique")
                # if it does not exist yet, replace key
                else:
                    instance.key.delete()  # delete key
                    instance.key = unique_key


class UniqueError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
