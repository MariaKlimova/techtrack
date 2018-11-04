import time
import random 

def timer( func ):
    def wrapper(*args, **kwargs ):
         start_ts = time.time()
         result = function( *args, **kwargs)
         end_ts = time.time()
         print( "time of execution of function '{}' is {} ms.".format( function.__name, 1000*(end_ts-start_ts))
         return result
    return wrapper

def sleeper(from_, to_):
    def sleeper_( function ):
        def wrapper(*args, **kwargs):
            time.sleep( random.randint( from_, to_ ) )
            result = function (*args, **kwargs)
            return result
        return wrapper
     return sleeper_

@timer
def foo( a, b ):
    return a + b

if __name__ == "__main__":
    print( foo (10, 5))
