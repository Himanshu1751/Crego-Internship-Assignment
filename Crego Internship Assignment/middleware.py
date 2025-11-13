import redis
from django.conf import settings

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

    def __call__(self, request):
        count = self.redis_client.incr('api_request_count')
        print(f"[RequestCounterMiddleware] Total API requests so far: {count}")
        return self.get_response(request)
