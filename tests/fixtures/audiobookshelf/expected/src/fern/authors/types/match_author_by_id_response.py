

import typing

from ...types.author import Author
from ...types.author_updated import AuthorUpdated

MatchAuthorByIdResponse = typing.Union[Author, typing.Optional[AuthorUpdated]]
