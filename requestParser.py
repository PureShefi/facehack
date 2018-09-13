#!/usr/bin/env python
import cgi
import urlparse
import router

def ParsePost(headerData):
    route, params = GetRoute(headerData.path), GetPostParameters(headerData)
    return router.urlRouter[route](params)

def ParseGet(headerData):
    route, params = GetRoute(headerData.path), GetGetParameters(headerData.path)
    return router.urlRouter[route](params)


def GetRoute(route):
    """
        Parses the route.
        example /index.php?asdasd=asdasdasd
        will return index.php
    """

    if "?" not in route:
        return route

    return route[:route.index("?")]

def GetGetParameters(route):
    """
        Parses the route get parameters
    """
    return urlparse.parse_qs(urlparse.urlparse(route).query)

def GetPostParameters(header):
    """
        Parses the header parameters of post
    """
    postVars = {}

    ctype, pdict = cgi.parse_header(header.headers.getheader('content-type'))

    if ctype == "multipart/form-data":
        postVars = cgi.parse_multipart(header.rfile, pdict)
    elif ctype == "application/x-www-form-urlencoded":
        content_length = int(header.headers['Content-Length']) # <--- Gets the size of data
        postVars = urlparse.parse_qs(header.rfile.read(content_length)) # <--- Gets the data itself

    return postVars
