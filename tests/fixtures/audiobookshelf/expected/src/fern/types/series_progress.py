

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .library_item_id import LibraryItemId


class SeriesProgress(UniversalBaseModel):
    """
    The user's progress of a series.
    """

    library_item_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[LibraryItemId]],
        FieldMetadata(alias="libraryItemIds"),
        pydantic.Field(alias="libraryItemIds", description="The IDs of the library items in the series."),
    ] = None
    """
    The IDs of the library items in the series.
    """

    library_item_ids_finished: typing_extensions.Annotated[
        typing.Optional[typing.List[LibraryItemId]],
        FieldMetadata(alias="libraryItemIdsFinished"),
        pydantic.Field(
            alias="libraryItemIdsFinished", description="The IDs of the library items in the series that are finished."
        ),
    ] = None
    """
    The IDs of the library items in the series that are finished.
    """

    is_finished: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isFinished"),
        pydantic.Field(alias="isFinished", description="Whether the series is finished."),
    ] = None
    """
    Whether the series is finished.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
