

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorDetail(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    Stable machine-readable error code.
    """

    message: str = pydantic.Field()
    """
    Human-readable error message.
    """

    details: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional structured context for the caller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
