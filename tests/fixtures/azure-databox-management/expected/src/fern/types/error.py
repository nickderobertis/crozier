

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    Top level error for the job.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code that can be used to programmatically identify the error.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Describes the error in detail and provides debugging information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
