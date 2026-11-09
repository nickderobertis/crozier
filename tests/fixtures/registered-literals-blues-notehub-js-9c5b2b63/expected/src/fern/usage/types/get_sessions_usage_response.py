

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.usage_sessions_data import UsageSessionsData
from ...types.usage_truncated_field import UsageTruncatedField


class GetSessionsUsageResponse(UniversalBaseModel):
    sessions: typing.List[UsageSessionsData]
    truncated: UsageTruncatedField

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
