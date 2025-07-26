from core.settings import REDIS
from redis import StrictRedis

redis = StrictRedis(host=REDIS['HOST'], port=REDIS['PORT'], db=0)
