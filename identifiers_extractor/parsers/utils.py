"""
Tree-sitter related functionality.
"""
import os
import urllib.request

from ..language_recognition.utils import identify_system
from tree_sitter import Language, Parser

DOWNLOAD_URLS = {
    "Linux":
        "https://github.com/areyde/buckwheat/releases/download/v1.1.1/tree-sitter-linux.tar.gz",
    "Darwin":
        "https://github.com/areyde/buckwheat/releases/download/v1.1.1/tree-sitter-darwin.tar.gz"
}

FILENAMES = {
    "Linux": "tree-sitter.tar.gz",
    "Darwin": "tree-sitter.tar.gz"
}

PARSERS = {}


def get_tree_sitter_dir() -> str:
    """
    Get tree-sitter directory.
    :return: absolute path.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "build"))


def get_tree_sitter_so() -> str:
    """
    Get build tree-sitter `.so` location.
    :return: absolute path.
    """
    return os.path.abspath(os.path.join(get_tree_sitter_dir(), "langs.so"))


def main() -> None:
    """
    Initialize tree-sitter library.
    :return: None.
    """
    system = identify_system()
    url = DOWNLOAD_URLS[system]
    filename = FILENAMES[system]
    if not os.path.exists(os.path.join(get_tree_sitter_dir(), filename)):
        urllib.request.urlretrieve(url,
                                   os.path.abspath(os.path.join(get_tree_sitter_dir(), filename)))
    if not os.path.exists(get_tree_sitter_so()):
        os.system("tar -xzf {tar} -C {directory}"
                  .format(tar=os.path.abspath(os.path.join(get_tree_sitter_dir(), filename)),
                          directory=get_tree_sitter_dir()))
    print("Parser successfully initialized.")


def get_parser(lang: str) -> Parser:
    """
    Initialize parser for a specific language.
    :param lang: language to use.
    :return: parser.
    """
    global PARSERS
    if lang not in PARSERS:
        parser = Parser()
        parser.set_language(Language(get_tree_sitter_so(), lang))
        PARSERS[lang] = parser
    else:
        parser = PARSERS[lang]
    return parser
