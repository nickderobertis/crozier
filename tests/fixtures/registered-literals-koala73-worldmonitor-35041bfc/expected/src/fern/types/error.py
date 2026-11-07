

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Error(UniversalBaseModel):
    """
    Error is returned when a handler encounters an error. It contains a simple error message that the developer can customize.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message (e.g., 'user not found', 'database connection failed')
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
