

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BookMetadataBase(UniversalBaseModel):
    """
    The base book metadata object for minified, normal, and extended schemas to inherit from.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the book. Will be null if unknown.
    """

    subtitle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subtitle of the book. Will be null if there is no subtitle.
    """

    genres: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The genres of the book.
    """

    published_year: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publishedYear"),
        pydantic.Field(alias="publishedYear", description="The year the book was published. Will be null if unknown."),
    ] = None
    """
    The year the book was published. Will be null if unknown.
    """

    published_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publishedDate"),
        pydantic.Field(alias="publishedDate", description="The date the book was published. Will be null if unknown."),
    ] = None
    """
    The date the book was published. Will be null if unknown.
    """

    publisher: typing.Optional[str] = pydantic.Field(default=None)
    """
    The publisher of the book. Will be null if unknown.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the book. Will be null if empty.
    """

    isbn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISBN of the book. Will be null if unknown.
    """

    asin: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ASIN of the book. Will be null if unknown.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language of the book. Will be null if unknown.
    """

    explicit: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the book has been marked as explicit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
