from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
with request.urlopen('https://www.douban.com') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
