from nntplib import NNTP_SSL

# Compression on:
s = NNTP_SSL('news.newshosting.com', 563, 'username', 'password'

# Compression off:
#s = NNTP_SSL('news.newshosting.com', 563, 'username', 'password',
#            None, False, 120, False)

# Select the group.
response, count, first, last, name = s.group('alt.binaries.teevee')
# Print the response.
print('Group', name, 'has', count, 'articles, range', first, 'to', last)

# Download some headers using XOVER.
response, headers = s.xover(660362, 660363)
# Print the response.
print(response)
# Print the parsed headers.
print(headers)

# Close the usenet connection.
response = s.quit()
# Print the response.
print(response)
