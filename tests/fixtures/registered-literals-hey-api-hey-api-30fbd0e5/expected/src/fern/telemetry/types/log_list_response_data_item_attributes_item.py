

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_list_response_data_item_attributes_item_value import LogListResponseDataItemAttributesItemValue


class LogListResponseDataItemAttributesItem(UniversalBaseModel):
    key: str
    value: LogListResponseDataItemAttributesItemValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
