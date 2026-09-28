

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fallout_metric import FalloutMetric


class FalloutYearSummary(UniversalBaseModel):
    """
    Fallout Year Summary.
    """

    year: int
    data: FalloutMetric

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
