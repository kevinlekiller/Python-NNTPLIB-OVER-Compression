Python-NNTPLIB-XOVER-Compression
================================

Quick implementation of header compression (For OVER and XOVER functions)
in python 3.3's nntplib, compression is enabled automatically after
connecting to usenet, you can disable compression completely by passing
a last argument (bool) when creating the NNTP or NNTP_SSL object.
See the example.py for how to disable it, leaving it enabled should
have no consequences however, it only affects XOVER/OVER.

If the server doesn't support compression headers will still be
downloaded, uncompressed.

If the server returns an empty compressed gzip string or if there is a
problem decompressing the data an NNTPDataError execption is thrown.
