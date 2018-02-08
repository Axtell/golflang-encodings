#!/usr/bin/env python3

import sys

CODE_PAGE_TEMPLATE = """CODEPAGE = {{
    {}
}}
"""

FILE_TEMPLATE = """NAME = {}

{}
"""


def code_page_from_string(s):
    """
    Generates a code page dict from a string
    Requires the string to be length-256
    :param s: the string representing the code page
    :return: a dict for the code page
    """
    code_page = {i: s[i] for i in range(256)}
    return code_page


def pretty_format(d):
    """
    Formats a code page dict to split on multiples of 8
    :param d: a code page dictionary
    :return: a pretty-formatted string representation of d
    """
    rows = []
    for i in range(256//8):
        row = {k: d[k] for k in range(i*8, (i+1)*8)}
        rows.append(repr(row)[1:-1])
    return CODE_PAGE_TEMPLATE.format(',\n    '.join(rows))


if __name__ == '__main__':
    outfile = sys.argv[1]
    name = ' '.join(sys.argv[2:])
    with open(outfile, 'w') as f:
        f.write(FILE_TEMPLATE.format(name, pretty_format(code_page_from_string(input()))))
