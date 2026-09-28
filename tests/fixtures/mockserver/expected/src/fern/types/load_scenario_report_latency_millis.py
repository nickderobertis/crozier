

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoadScenarioReportLatencyMillis(UniversalBaseModel):
    p50: typing.Optional[int] = None
    p95: typing.Optional[int] = None
    p99: typing.Optional[int] = None
    p999: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
