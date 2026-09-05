

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1metrics_count_value_value import V1Alpha1MetricsCountValueValue


class V1Alpha1MetricsCountValue(UniversalBaseModel):
    attributes: typing.Dict[str, typing.Any]
    start_time_unix_nano: int
    time_unix_nano: int
    value: V1Alpha1MetricsCountValueValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
