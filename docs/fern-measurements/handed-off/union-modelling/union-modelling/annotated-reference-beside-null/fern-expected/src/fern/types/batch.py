

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_status import BatchStatus
from .batch_totals import BatchTotals


class Batch(UniversalBaseModel):
    id: str
    status: typing.Optional[BatchStatus] = None
    totals: typing.Optional[BatchTotals] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
