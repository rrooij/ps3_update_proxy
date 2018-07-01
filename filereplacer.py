#!/usr/bin/env python3

"""
Replace content of a URL with a specific file

Copyright (C) 2018 rrooij

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

"""

from mimetypes import guess_type
from mitmproxy import http
from os.path import dirname, realpath


script_path = dirname(realpath(__file__))
file_lines = open(script_path + '/files.txt', 'r').read().splitlines()
files = { x.split('|')[0]: x.split('|')[1] for x in file_lines }

def request(flow: http.HTTPFlow) -> None:
    # Check if url is in list
    if flow.request.pretty_url in files:
        replacement_file = files[flow.request.pretty_url]
        mime = guess_type(replacement_file, False)
        try:
            file_content = open(script_path + '/' + replacement_file, 'rb').read()
            flow.response = http.HTTPResponse.make(
                200,
                file_content,
                {"Content-Type": mime[0]}
            )
        except OSError:
            print("{} could not be opened".format(replacement_file))
