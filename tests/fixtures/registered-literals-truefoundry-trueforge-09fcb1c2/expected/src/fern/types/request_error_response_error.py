

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RequestErrorResponseError(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional machine-readable error code; null when not applicable.
    """

    message: str = pydantic.Field()
    """
    Human-readable explanation of the failure.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional request field that caused the error; null when not field-specific.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional error category (e.g. validation vs conflict).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
