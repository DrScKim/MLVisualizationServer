import time
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def calc_duration(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.time()
        r = original_function(*args, **kwargs)
        end = time.time()
        duration = "%s" % (end-start)
        logging.info ("function({}) duration time: {}".format(original_function.__name__, duration))
        return r
    return wrapper_function
