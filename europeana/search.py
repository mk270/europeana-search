
#  EuropeanaSearch, a trivial wrapper around the Europeana search API, 
#  by Martin Keegan
#
#  Copyright (C) 2013  Martin Keegan
#
#  This programme is free software; you may redistribute and/or modify
#  it under the terms of the Apache Software Licence v2.0

import requests

prefix = 'http://preview.europeana.eu/api/v2/search.json'

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
        for i in self.query(self.api_key, query)['items']:
            yield i['edmPreview'][0]
