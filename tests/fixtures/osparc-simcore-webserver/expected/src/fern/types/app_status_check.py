

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AppStatusCheck(UniversalBaseModel):
    app_name: str = pydantic.Field()
    """
    Application name
    """

    version: str = pydantic.Field()
    """
    Application's version
    """

    services: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Other backend services connected from this service
    """

    sessions: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Client sessions info. If single session per app, then is denoted as main
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to current resource
    """

    diagnostics_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to diagnostics report sub-resource. This MIGHT take some time to compute
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
