

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StatusEvent(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable status message
    """

    digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content digest associated with the status, if applicable
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of bytes expected for the operation
    """

    completed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of bytes transferred so far
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
