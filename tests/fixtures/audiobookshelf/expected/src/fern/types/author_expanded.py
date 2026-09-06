

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .author import Author


class AuthorExpanded(Author):
    """
    The author schema with the total number of books in the library.
    """

    num_books: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numBooks"),
        pydantic.Field(alias="numBooks", description="The number of books associated with the author in the library."),
    ] = None
    """
    The number of books associated with the author in the library.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
