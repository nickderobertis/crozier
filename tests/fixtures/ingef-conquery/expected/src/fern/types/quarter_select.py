

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .select_base import SelectBase
from .temporal_sampler import TemporalSampler


class QuarterSelect(SelectBase):
    """
    Emits the sampled quarter in `2020Q1` format.
    """

    sample: typing.Optional[TemporalSampler] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
