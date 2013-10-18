Python-NNTPLIB-XOVER-Compression
================================

Really quick implementation of header compression in python 3.3's nntplib
written in about an hour, you might want to try to catch zlib exceptions,
you can also add the compression function to run when connecting so
you don't have to call it every time you connect.

I used XOVER since I haven't seen any providers supporting OVER,
you can modify OVER if you want.
