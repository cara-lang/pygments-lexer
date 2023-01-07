"""
Lexer for the Cara programming language.

:copyright: Copyright 2022 Martin Janiczek (@janiczek)
:license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words, include, bygroups
from pygments.token import Comment, Keyword, Name, Number, Punctuation, \
    String, Whitespace

__all__ = ['CaraLexer']


class CaraLexer(RegexLexer):
    """
    For Cara source code.
    """

    name = 'Cara'
    url = 'http://cara-lang.com/'
    aliases = ['cara']
    filenames = ['*.cara']
    mimetypes = ['text/x-cara']

    validName = r'[a-z_][a-zA-Z0-9_\']*'

    specialName = r'^main(?=[(])'

    builtinOps = (
        '!=', '!',
        '||', '|>', '|',
        '^',
        '\\', '\'',
        '>>>', '>>', '>=', '>',
        '==', '=',
        '<=', '<<<', '<<', '<-', '<',
        '::', ':',
        '/',
        '...', '..', '.',
        '->', '-',
        '++', '+',
        '*',
        '&&',
        '%',
    )

    reservedWords = words((
        'alias', 'as',
        'case',
        'else',
        'if',
        'module',
        'of', 'opaque',
        'private',
        'test', 'then', 'type',
        'where', 'with',
    ), suffix=r'\b')

    tokens = {
        'root': [

            # Comments
            (r'/\*', Comment.Multiline, 'comment'),
            (r'//.*', Comment.Single),
            (r'#!.*', Comment.Single),

            # Whitespace
            (r'\s+', Whitespace),

            # Strings
            (r'"', String, 'doublequote'),

            # Keywords
            (reservedWords, Keyword.Reserved),

            # Types
            (r'[A-Z][a-zA-Z0-9_]*', Keyword.Type),

            # Main
            (specialName, Keyword.Reserved),

            # Prefix Operators
            (words((builtinOps), prefix=r'\(', suffix=r'\)'), Name.Function),

            # Infix Operators
            (words(builtinOps), Name.Function),

            # Numbers
            include('numbers'),

            # Variable Names
            (validName, Name.Variable),

            # Parens
            (r'[,()\[\]{}]', Punctuation),

        ],

        'comment': [
            (r'\*(?!/)', Comment.Multiline),
            (r'/\*', Comment.Multiline, 'comment'), # TODO isn't this duplicated above?
            (r'[^*/]', Comment.Multiline),
            (r'\*/', Comment.Multiline, '#pop'),
        ],

        'doublequote': [
            # TODO interpolation: $xyz and ${xyz.abc}
            (r'\\u[0-9a-fA-F]{4}', String.Escape),
            (r'\\[nrt\\"]', String.Escape),
            (r'[^"]', String),
            (r'"', String, '#pop'),
        ],

        'numbers': [
            # TODO scientific notation
            # TODO 0x, 0o, 0b
            # TODO why did the Elm lexer have _ instead of - in these?
            (r'-?\d+\.(?=\d+)', Number.Float),
            (r'-?\d+', Number.Integer),
        ],
    }
