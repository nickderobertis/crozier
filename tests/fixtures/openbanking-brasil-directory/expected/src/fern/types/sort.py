

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sort_order_by_item import SortOrderByItem


class Sort(UniversalBaseModel):
    order_by: typing_extensions.Annotated[
        typing.Optional[typing.List[SortOrderByItem]], FieldMetadata(alias="orderBy"), pydantic.Field(alias="orderBy")
    ] = None
    sorted: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
