from ferris import Controller, messages, route_with
from app.models.post import Post
import requests
import time


API_HOSTNAME = "http://hn.algolia.com"
API_VERSION = "v1"
FREQUENCY = 86400  # fetches daily


class Cron(Controller):
    class Meta:
        Model = Post
        components = (messages.Messaging,)
        prefixes = ('api',)

    @route_with('/api/cron/fetch_news')
    def api_fetch_news(self):
        ts = int(time.time()) - FREQUENCY
        action = "search_by_date?query=angular&tags=story&numericFilters=created_at_i>%s" % ts
        url = "%s/api/%s/%s" % (API_HOSTNAME, API_VERSION, action,)
        r = requests.get(url)
        data = r.json()
        print data
