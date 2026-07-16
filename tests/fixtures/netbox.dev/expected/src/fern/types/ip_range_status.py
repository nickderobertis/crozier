

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_range_status_label import IpRangeStatusLabel
from .ip_range_status_value import IpRangeStatusValue


class IpRangeStatus(UniversalBaseModel):
    label: IpRangeStatusLabel
    value: IpRangeStatusValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
