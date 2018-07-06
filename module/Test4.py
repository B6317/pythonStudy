# coding=utf-8
# create by toonew at 2018/7/6

# 可选导入（Optional imports）
try:
    from http.client import responses
except ImportError:
    try:
        from httplib import responses
    except ImportError:
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH

        responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])
