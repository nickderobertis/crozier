

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .book_metadata_base import BookMetadataBase


class BookMetadataMinified(BookMetadataBase):
    """
    The minified metadata for a book in the database.
    """

    title_ignore_prefix: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="titleIgnorePrefix"),
        pydantic.Field(
            alias="titleIgnorePrefix", description="The title of the book with any prefix moved to the end."
        ),
    ] = None
    """
    The title of the book with any prefix moved to the end.
    """

    author_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="authorName"),
        pydantic.Field(alias="authorName", description="The name of the book's author(s)."),
    ] = None
    """
    The name of the book's author(s).
    """

    author_name_lf: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="authorNameLF"),
        pydantic.Field(alias="authorNameLF", description="The name of the book's author(s) with last names first."),
    ] = None
    """
    The name of the book's author(s) with last names first.
    """

    narrator_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="narratorName"),
        pydantic.Field(alias="narratorName", description="The name of the audiobook's narrator(s)."),
    ] = None
    """
    The name of the audiobook's narrator(s).
    """

    series_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="seriesName"),
        pydantic.Field(alias="seriesName", description="The name of the book's series."),
    ] = None
    """
    The name of the book's series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
