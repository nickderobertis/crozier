

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StRetryConf(UniversalBaseModel):
    num_retries: typing.Optional[float] = None
    retry_interval_seconds: typing.Optional[float] = None
    timeout_seconds: typing.Optional[float] = None
    tolerance_seconds: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
