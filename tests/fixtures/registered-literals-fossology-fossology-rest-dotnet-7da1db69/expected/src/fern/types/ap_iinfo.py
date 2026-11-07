

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApIinfo(UniversalBaseModel):
    """
    Api Documentation
    """

    openapi: typing.Optional[str] = pydantic.Field(default=None)
    """
    version
    """

    info: typing.Optional[str] = pydantic.Field(default=None)
    """
    version info
    """

    servers: typing.Optional[str] = pydantic.Field(default=None)
    """
    server info
    """

    security: typing.Optional[str] = pydantic.Field(default=None)
    """
    security info
    """

    tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    API tags
    """

    paths: typing.Optional[str] = pydantic.Field(default=None)
    """
    API endpoints
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
