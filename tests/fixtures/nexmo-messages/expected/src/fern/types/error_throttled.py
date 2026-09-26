

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorThrottled(UniversalBaseModel):
    detail: str = pydantic.Field()
    """
    Additional information about the error
    """

    instance: str = pydantic.Field()
    """
    Internal Trace ID
    """

    title: str = pydantic.Field()
    """
    Generic error message
    """

    type: str = pydantic.Field()
    """
    Link to error / remediation options
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
