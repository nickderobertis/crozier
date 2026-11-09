

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.usage_truncated_field import UsageTruncatedField
from .get_data_usage_response_data_item import GetDataUsageResponseDataItem


class GetDataUsageResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetDataUsageResponseDataItem]] = None
    truncated: typing.Optional[UsageTruncatedField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
