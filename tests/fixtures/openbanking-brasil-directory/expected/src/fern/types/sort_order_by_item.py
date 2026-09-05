

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sort_order_by_item_direction import SortOrderByItemDirection


class SortOrderByItem(UniversalBaseModel):
    ascending: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether ascending
    """

    direction: typing.Optional[SortOrderByItemDirection] = pydantic.Field(default=None)
    """
    Direction of sort, i.e. ascending or descending
    """

    ignore_case: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ignoreCase"),
        pydantic.Field(alias="ignoreCase", description="Was the case ignored"),
    ] = None
    """
    Was the case ignored
    """

    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the property used for sorting
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
