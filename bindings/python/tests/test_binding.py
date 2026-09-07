from unittest import TestCase

import tree_sitter_just

from tree_sitter import Language, Parser


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        Parser(Language(tree_sitter_just.language()))
