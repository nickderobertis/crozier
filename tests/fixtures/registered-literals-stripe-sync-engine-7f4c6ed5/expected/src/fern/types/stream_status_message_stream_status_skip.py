

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StreamStatusMessageStreamStatusSkip(UniversalBaseModel):
    stream: str = pydantic.Field()
    """
    Stream being reported on.
    """

    reason: str = pydantic.Field()
    """
    Why the stream was skipped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
