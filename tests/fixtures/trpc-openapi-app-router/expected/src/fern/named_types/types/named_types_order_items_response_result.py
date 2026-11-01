

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .named_types_order_items_response_result_data import NamedTypesOrderItemsResponseResultData


class NamedTypesOrderItemsResponseResult(UniversalBaseModel):
    data: NamedTypesOrderItemsResponseResultData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
