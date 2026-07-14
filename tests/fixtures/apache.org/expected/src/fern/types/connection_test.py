

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectionTest(UniversalBaseModel):
    """
    Connection test results.

    *New in version 2.2.0*
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The success or failure message of the request.
    """

    status: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The status of the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
