"""Doctest configuration."""

from doctest import ELLIPSIS, NORMALIZE_WHITESPACE

from sybil import Sybil
from sybil.parsers.markdown import PythonCodeBlockParser, SkipParser
from sybil.parsers.rest import DocTestParser

pytest_collect_file = Sybil(
    parsers=[
        DocTestParser(optionflags=ELLIPSIS | NORMALIZE_WHITESPACE),
        PythonCodeBlockParser(),
        SkipParser(),
    ],
    patterns=["*.md", "*.py"],
).pytest()
