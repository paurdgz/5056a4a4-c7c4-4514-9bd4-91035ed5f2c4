import functools
import json
import time

from difflib import SequenceMatcher


def pretty_print(logger):
    pass


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            output = func(*args, **kwargs)
            logger.info("[Execution time (seconds)][%s]" % (time.time() - start))
            return output
        return wrapper
    return decorator


class StringWrapper(object):
    DEFAULT_THRESHOLD = 0.5

    class Decorators:
        @staticmethod
        def sensitivity_matching_meta_decorator():
            def decorator(func):
                @functools.wraps(func)
                def wrapper(self, pattern, *args, **kwargs):
                    pattern = self._sensitivity_matching(string=pattern)
                    return func(self, pattern, *args, **kwargs)
                return wrapper
            return decorator

    def __init__(self, value, case_sensitive=False, default_similarity_threshold=DEFAULT_THRESHOLD):
        self.default_similarity_threshold = default_similarity_threshold
        self.case_sensitive = case_sensitive
        self._value = value

    def _sensitivity_matching(self, string):
        return string if self.case_sensitive else string.lower()

    @property
    def value(self):
        return self._sensitivity_matching(self._value)

    def contains (pattern, reverse=False):
        pass