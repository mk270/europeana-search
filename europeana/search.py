
#  EuropeanaSearch, a trivial wrapper around the Europeana search API, 
#  by Martin Keegan
#
#  Copyright (C) 2013  Martin Keegan
#
#  This programme is free software; you may redistribute and/or modify
#  it under the terms of the Apache Software Licence v2.0

import requests

prefix = 'http://preview.europeana.eu/api/v2/search.json'
resource_prefix = 'http://preview.europeana.eu/api/v2/record'

class Search(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def query(self, query):
        args = { 
            'wskey': self.api_key, 
            'query': query, 
            'start': '1', 
            'rows': '12', 
            'profile': 'standard'
            }
        r = requests.get(prefix, params=args)
        return r.json()

    def preview_urls(self, query):
        for i in self.query(query)['items']:
            yield i['edmPreview'][0]

    def resources(self, query):
        def gen_search_results():
            start = 1
            batch_size = 12

            while True:
                args = {
                    'wskey': self.api_key, 
                    'query': query, 
                    'start': str(start), 
                    'rows': str(batch_size), 
                    'profile': 'standard'
                    }
                start += batch_size
                results = requests.get(prefix, params=args).json()

                item_count = int(results["itemsCount"])
                for i in xrange(0, item_count):
                    yield results["items"][i]

        for item in gen_search_results():
            args = {
                'wskey': self.api_key, 
                'profile': 'full'
                }
            url = "%s%s.json" % (resource_prefix, item["id"])

            result = requests.get(url, params=args).json()
            yield result
