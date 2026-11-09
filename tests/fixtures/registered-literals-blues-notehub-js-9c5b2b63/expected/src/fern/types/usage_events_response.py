

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .usage_events_data import UsageEventsData
from .usage_truncated_field import UsageTruncatedField


class UsageEventsResponse(UniversalBaseModel):
    data: typing.List[UsageEventsData]
    truncated: typing.Optional[UsageTruncatedField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
