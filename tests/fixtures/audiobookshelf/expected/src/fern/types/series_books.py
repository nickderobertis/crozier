

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .library_item_sequence import LibraryItemSequence
from .series_id import SeriesId
from .series_name import SeriesName


class SeriesBooks(UniversalBaseModel):
    """
    A series object which includes the name and books in the series.
    """

    id: typing.Optional[SeriesId] = None
    name: typing.Optional[SeriesName] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    name_ignore_prefix: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nameIgnorePrefix"),
        pydantic.Field(
            alias="nameIgnorePrefix", description="The name of the series with any prefix moved to the end."
        ),
    ] = None
    """
    The name of the series with any prefix moved to the end.
    """

    name_ignore_prefix_sort: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nameIgnorePrefixSort"),
        pydantic.Field(alias="nameIgnorePrefixSort", description="The name of the series with any prefix removed."),
    ] = None
    """
    The name of the series with any prefix removed.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Will always be `series`.
    """

    books: typing.Optional[typing.List[LibraryItemSequence]] = pydantic.Field(default=None)
    """
    The library items that contain the books in the series. A sequence attribute that denotes the position in the series the book is in, is tacked on.
    """

    total_duration: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalDuration"),
        pydantic.Field(
            alias="totalDuration", description="The combined duration (in seconds) of all books in the series."
        ),
    ] = None
    """
    The combined duration (in seconds) of all books in the series.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
