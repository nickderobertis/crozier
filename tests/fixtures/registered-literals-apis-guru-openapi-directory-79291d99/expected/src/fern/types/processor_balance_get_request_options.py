

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .min_last_updated_datetime import MinLastUpdatedDatetime


class ProcessorBalanceGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/processor/balance/get` results.
    """

    min_last_updated_datetime: typing.Optional[MinLastUpdatedDatetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
