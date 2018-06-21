record = [{'url': 'http://google.com', 'method': 'GET', 'count': 3},
          {'url': 'http://google.com', 'method': 'POST', 'count': 2},
          {'url': 'httpS://wp.com', 'method': 'GET', 'count': 5}]

expected = {}

for i in record:
    key = (i['url'], i['method'])
    expected[key] = i['count']