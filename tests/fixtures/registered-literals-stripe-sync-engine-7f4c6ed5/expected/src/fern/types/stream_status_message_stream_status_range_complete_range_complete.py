

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StreamStatusMessageStreamStatusRangeCompleteRangeComplete(UniversalBaseModel):
    """
    The sub-range that finished.
    """

    gte: str = pydantic.Field()
    """
    Inclusive lower bound (ISO 8601).
    """

    lt: str = pydantic.Field()
    """
    Exclusive upper bound (ISO 8601).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
