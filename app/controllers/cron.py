from ferris import Controller, messages, route_with
from app.models.post import Post


class Cron(Controller):
    class Meta:
        Model = Post
        components = (messages.Messaging,)
        prefixes = ('api',)

    @route_with('/api/cron/fetch_news')
    def api_fetch_news(self):
        pass
