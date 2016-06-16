import http.client
import urllib
import urllib.request
import json


class MovieClient():
    def __init__(self):
        self.conn = http.client.HTTPConnection("api.douban.com")

    def search(self, keyword):

        url = "/v2/movie/search?count=5&q=%s" % urllib.parse.quote(keyword)
        self.conn.request('GET', url)
        response = self.conn.getresponse()
        data = response.read()
        self.conn.close()
        jsonData = json.loads(data.decode())
        if 'subjects' in jsonData:
            return jsonData['subjects']
        else:
            return 0
