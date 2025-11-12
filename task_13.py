import time


def cached(max_size= None, seconds= None):

    def decorator(func):
        cache = {}


        def wrapper(*args, **kwargs):

            if args in cache :
                return cache[args][0], len(cache) ,  cache

            if(len(cache) == max_size):
               del cache[next(iter(cache))]

            result = func(*args, **kwargs)
            cache[args] = [result, time.time()]

            return result , len(cache), cache

        return wrapper

    return decorator


@cached(max_size=3, seconds=10)
def slow_function(x):
    return x ** 2


print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
print(slow_function(2))  # Вывод: 4 (без вычисления)
time.sleep(2)
print(slow_function(3))  # Вывод: "Вычисляю для 2..." → 4
print(slow_function(7))
print(slow_function(4))
print(slow_function(8))
