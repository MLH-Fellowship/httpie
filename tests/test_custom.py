import argparse
import json
import os
from tempfile import gettempdir
from urllib.request import urlopen

import pytest

from httpie.cli.argtypes import (
    PARSED_DEFAULT_FORMAT_OPTIONS,
    parse_format_options,
)
from httpie.cli.definition import parser
from httpie.output.formatters.colors import get_lexer
from httpie.status import ExitStatus
from utils import COLOR, CRLF, HTTP_OK, MockEnvironment, http


class TestPrettyOptions:
    """Test the --pretty handling."""

    def test_pretty_enabled_by_default(self, httpbin):
        env = MockEnvironment(colors=256)
        r = http('GET', httpbin.url + '/get', env=env)
        assert COLOR in r

    # def test_pretty_enabled_by_default_unless_stdout_redirected(self, httpbin):
    #     r = http('GET', httpbin.url + '/get')
    #     assert COLOR not in r

    def test_force_pretty(self, httpbin):
        env = MockEnvironment(stdout_isatty=False, colors=256)
        r = http('--pretty=all', 'GET', httpbin.url + '/get | more', env=env, )
        test = env.stdout_isatty
        test_type = type(env.stdout_isatty)
        test2 = env.stdout_fstat
        # print(env.stdout_isatty, type(env.stdout_isatty))
        assert COLOR in r

    # def test_force_ugly(self, httpbin):
    #     r = http('--pretty=none', 'GET', httpbin.url + '/get')
    #     assert COLOR not in r

    # def test_subtype_based_pygments_lexer_match(self, httpbin):
    #     """Test that media subtype is used if type/subtype doesn't
    #     match any lexer.

    #     """
    #     print("test")
    #     env = MockEnvironment(colors=256)
    #     r = http('--print=B', '--pretty=all', httpbin.url + '/post',
    #              'Content-Type:text/foo+json', 'a=b', env=env)
    #     assert COLOR in r

    # def test_colors_option(self, httpbin):
    #     env = MockEnvironment(colors=256)
    #     r = http('--print=B', '--pretty=colors',
    #              'GET', httpbin.url + '/get', 'a=b',
    #              env=env)
    #     # Tests that the JSON data isn't formatted.
    #     assert not r.strip().count('\n')
    #     assert COLOR in r

    # def test_format_option(self, httpbin):
    #     env = MockEnvironment(colors=256)
    #     r = http('--print=B', '--pretty=format',
    #              'GET', httpbin.url + '/get', 'a=b',
    #              env=env)
    #     # Tests that the JSON data is formatted.
    #     assert r.strip().count('\n') == 2
    #     assert COLOR not in r
