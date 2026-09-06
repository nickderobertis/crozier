

import typing

from ...types.author import Author
from ...types.author_merged import AuthorMerged
from ...types.author_updated import AuthorUpdated

UpdateAuthorByIdResponse = typing.Union[Author, typing.Optional[AuthorUpdated], typing.Optional[AuthorMerged]]
