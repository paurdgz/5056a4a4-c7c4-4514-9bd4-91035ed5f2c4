import logging
import json
import fire

from model import SIC
from util import StringWrapper, pretty_print, timeit


URL = "https://www.osha.gov/pls/imis/sic_manual.html"
DEFAULT_INDUSTRY_FILE = "industries.json"

logger = logging.getLogger(__name__)



class Main(object):


    def _recursive_search(self, node, string_wrapper, exact):
         title = node["title"]
        children = node["children"]
        new_children = []
        for child in children:
            child_valid = self._recursive_search(child, string_wrapper, exact=exact)
            if child_valid:
                new_children.append(child)
        node["children"] = new_children
        result = len(new_children) or string_wrapper.boolean_search(title, reverse=True, exact=exact)
        return result


    @staticmethod
    @timeit(logger)

    def search(self, title, exact=False, filename=DEFAULT_INDUSTRY_FILE):
        target_title = StringWrapper(value=title)
        sic_industries = SIC.load_json(filename)
        return []  # return list of the matching industries
        new_children = []
        for child in children:
            if self._recursive_search(child, target_title, exact=exact):
                new_children.append(child)
        return new_children




if __name__ == "__main__":	if __name__ == "__main__":
