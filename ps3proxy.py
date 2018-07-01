"""
Replace Sony's update response with an own response.

This prevents the need for updating when using PSN.
"""
from mitmproxy import http
from os.path import dirname, realpath

script_path = dirname(realpath(__file__))

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "http://feu01.ps3.update.playstation.net/update/ps3/list/eu/ps3-updatelist.txt":
        flow.response.content = open(script_path + '/eu.txt', 'rb').read()
    elif flow.request.pretty_url == "http://fus01.ps3.update.playstation.net/update/ps3/list/us/ps3-updatelist.txt":
        flow.response.content = open(script_path + '/us.txt', 'rb').read()
