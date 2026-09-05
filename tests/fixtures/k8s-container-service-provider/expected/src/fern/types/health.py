

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Health(UniversalBaseModel):
    """
    Health status singleton resource
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource type identifier
    """

    status: str = pydantic.Field()
    """
    Health status
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Canonical path of the resource
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service provider build version
    """

    uptime: typing.Optional[int] = pydantic.Field(default=None)
    """
    Seconds since the service provider started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
