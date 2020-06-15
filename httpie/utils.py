from __future__ import division

import json
import mimetypes
import time
from collections import OrderedDict
from http.cookiejar import parse_ns_headers
from pprint import pformat
from typing import List, Tuple

import requests.auth


def load_json_preserve_order(s):
    return json.loads(s, object_pairs_hook=OrderedDict)


def repr_dict(d: dict) -> str:
    return pformat(d)


def humanize_bytes(n, precision=2):
    # Author: Doug Latornell
    # Licence: MIT
    # URL: https://code.activestate.com/recipes/577081/
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 B'
    >>> humanize_bytes(1024, precision=1)
    '1.0 kB'
    >>> humanize_bytes(1024 * 123, precision=1)
    '123.0 kB'
    >>> humanize_bytes(1024 * 12342, precision=1)
    '12.1 MB'
    >>> humanize_bytes(1024 * 12342, precision=2)
    '12.05 MB'
    >>> humanize_bytes(1024 * 1234, precision=2)
    '1.21 MB'
    >>> humanize_bytes(1024 * 1234 * 1111, precision=2)
    '1.31 GB'
    >>> humanize_bytes(1024 * 1234 * 1111, precision=1)
    '1.3 GB'

    """
    abbrevs = [
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'B')
    ]

    if n == 1:
        return '1 B'

    for factor, suffix in abbrevs:
        if n >= factor:
            break

    # noinspection PyUnboundLocalVariable
    return '%.*f %s' % (precision, n / factor, suffix)


class ExplicitNullAuth(requests.auth.AuthBase):
    """Forces requests to ignore the ``.netrc``.
    <https://github.com/psf/requests/issues/2773#issuecomment-174312831>
    """

    def __call__(self, r):
        return r


def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.

    """
    mime, encoding = mimetypes.guess_type(filename, strict=False)
    if mime:
        content_type = mime
        if encoding:
            content_type = '%s; charset=%s' % (mime, encoding)
        return content_type


def get_expired_cookies(headers: List[Tuple[str, str]], curr_timestamp: float = None) -> List[dict]:
    expired_cookies = []
    cookie_headers = []
    curr_timestamp = curr_timestamp or time.time()

    for header_name, content in headers:
        if header_name == 'Set-Cookie':
            cookie_headers.append(content)

    extracted_cookies = [
        dict(cookie, name=cookie[0][0])
        for cookie in parse_ns_headers(cookie_headers)
    ]

    for cookie in extracted_cookies:
        if "expires" in cookie and cookie['expires'] <= curr_timestamp:
            expired_cookies.append({
                'name': cookie['name'],
                'path': cookie.get('path', '/')
            })

    return expired_cookies
