from nntplib import NNTP_SSL

s = NNTP_SSL('news.newshosting.com', 563, 'username', 'password')

response, count, first, last, name = s.group('alt.binaries.teevee')

print('Group', name, 'has', count, 'articles, range', first, 'to', last)

response, headers = s.xover(660362, 660363)

print(response)
print(headers)

response = s.quit()
print(resp)
