

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CheckAdvisoriesResponseActiveAdvisoriesItem(UniversalBaseModel):
    advisory_id: typing.Optional[str] = None
    severity: typing.Optional[str] = None
    action: typing.Optional[str] = None
    affected_algorithms: typing.Optional[typing.List[str]] = None
    grace_period_expired: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
