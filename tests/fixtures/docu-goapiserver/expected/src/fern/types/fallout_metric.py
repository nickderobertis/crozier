

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FalloutMetric(UniversalBaseModel):
    """
    Fallout Metric.
    """

    year: int
    pre_registered: int
    withdrew_same_year: int
    fallout_rate: typing.Optional[float] = None
    yoy_delta: typing.Optional[float] = None
    is_ytd: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
