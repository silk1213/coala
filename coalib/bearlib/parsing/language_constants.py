"""
This file contains tables that provide useful constants for specific languages.

Each dictionary holds constants for some elements of the LANGUAGE enum. If
the element is empty, there are no such things for this language. If no
element is available yet, consider adding it yourself.
"""
from coalib.misc.Enum import enum

"""
This enum holds all languages for which the bearlib provides constants.
"""
LANGUAGES = enum(
    "C",
    "CSHARP",
    "CPP",
    "PYTHON3",
    "PYTHON2",
    "VALA",
    "JAVA",
    "OCTAVE",
    "MATLAB",
    "BASH",
    "PHP",
    "TEX")

"""
This dictionary holds for each LANGUAGE a dict with the beginning indication
of a multiline string as the key and the associated end delimiter as the value.
"""
MULTILINE_STRING_DELIMITERS = {
    LANGUAGES.PYTHON3: {'"""': '"""',
                        "'''": "'''"},
    LANGUAGES.CPP: {'R("': ')"'}}

"""
This dictionary holds for each LANGUAGE a dict with the beginning indication
of a single line string as key and the associated end delimiter as the value.
"""
STRING_DELIMITERS = {
    LANGUAGES.PYTHON3: {'"': '"',
                        "'": "'"},
    LANGUAGES.C: {'"': '"'},
    LANGUAGES.CPP: {'"': '"'}}

"""
This dictionary holds for each LANGUAGE a list of delimiters usable for a
single-line comment.
"""
COMMENT_DELIMITER = {
    LANGUAGES.PYTHON3: ['#'],
    LANGUAGES.C: ["//"],
    LANGUAGES.CPP: ["//"]}

"""
This dictionary holds for each LANGUAGE a dict with the beginning indication of
a multiline comment as key and the associated end delimiter as the value.
"""
MULTILINE_COMMENT_DELIMITERS = {
    LANGUAGES.PYTHON3: {},
    LANGUAGES.C: {"/*": "*/"},
    LANGUAGES.CPP: {"/*": "*/"}}
