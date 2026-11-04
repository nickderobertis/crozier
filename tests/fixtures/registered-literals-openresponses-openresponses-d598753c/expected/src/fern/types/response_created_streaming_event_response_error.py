

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResponseCreatedStreamingEventResponseError(UniversalBaseModel):
    """
    The error that occurred, if the response failed.
    """

    code: str = pydantic.Field()
    """
    A machine-readable error code that was returned.
    """

    message: str = pydantic.Field()
    """
    A human-readable description of the error that was returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
