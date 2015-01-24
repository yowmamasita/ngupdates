from ferris import Controller, messages, route_with
from app.models.post import Post
import requests
import time


API_HOSTNAME = "http://hn.algolia.com"
API_VERSION = "v1"
FREQUENCY = 86400  # fetches daily
POINTS = 50


class Cron(Controller):
    class Meta:
        Model = Post
        components = (messages.Messaging,)
        prefixes = ('api',)

    @route_with('/api/cron/fetch_news')
    def api_fetch_news(self):
        search = "angular"
        ts = int(time.time()) - FREQUENCY
        num_filter = "points>%s,created_at_i>%s" % (POINTS, ts,)
        action = "search_by_date?query=%s&tags=story&numericFilters=%s" % (search, num_filter,)
        url = "%s/api/%s/%s" % (API_HOSTNAME, API_VERSION, action,)
        r = requests.get(url)
        data = r.json()
        print data
