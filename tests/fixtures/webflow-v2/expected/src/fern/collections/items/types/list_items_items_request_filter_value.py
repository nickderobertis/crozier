

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .list_items_items_request_filter_value_exists import ListItemsItemsRequestFilterValueExists
from .list_items_items_request_filter_value_in import ListItemsItemsRequestFilterValueIn
from .list_items_items_request_filter_value_nin import ListItemsItemsRequestFilterValueNin


class ListItemsItemsRequestFilterValue(UniversalBaseModel):
    eq: typing.Optional[str] = None
    ne: typing.Optional[str] = None
    gt: typing.Optional[str] = None
    gte: typing.Optional[str] = None
    lt: typing.Optional[str] = None
    lte: typing.Optional[str] = None
    in_: typing_extensions.Annotated[
        typing.Optional[ListItemsItemsRequestFilterValueIn], FieldMetadata(alias="in"), pydantic.Field(alias="in")
    ] = None
    nin: typing.Optional[ListItemsItemsRequestFilterValueNin] = None
    contains: typing.Optional[str] = None
    ncontains: typing.Optional[str] = None
    exists: typing.Optional[ListItemsItemsRequestFilterValueExists] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
