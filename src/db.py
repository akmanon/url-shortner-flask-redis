import redis
import time


class ConnectRedis:
    def __init__(self) -> None:
        self.redis_pool = redis.ConnectionPool(
            host="localhost",
            port=6379,
            decode_responses=True,
            socket_connect_timeout=1,
        )

        pass

    def get_conn(self) -> redis.client.Redis:
        return redis.Redis(
            connection_pool=self.redis_pool,
        )

    def set_url(self, url_hash, url_user) -> bool:
        try:
            r = self.get_conn()
            r.set(url_hash, url_user)
            return True
        except redis.ConnectionError as err:
            print(f"Connection Error connecting Redis :: {err}")
        except Exception as err1:
            print(f"Unexpected Error while connecting to Redis :: {err1}")
        return False

    def get_url(self, url_hash) -> str | None:
        try:
            r = self.get_conn()
            return r.get(url_hash)
        except redis.ConnectionError as err:
            print(f"Connection Error connecting Redis :: {err}")
        except Exception as err1:
            print(f"Unexpected Error while connecting to Redis :: {err1}")
        return None


if __name__ == "__main__":

    r = ConnectRedis()
    # for i in range(100000):
    #     r.set_url(str(i), )
    t = []
    s_t = time.time()
    for i in range(10000):
        t.append(r.get_url(str(i + 2)))
    e_t = time.time()
    print(f"Result = {t}, time taken : {e_t - s_t}")
