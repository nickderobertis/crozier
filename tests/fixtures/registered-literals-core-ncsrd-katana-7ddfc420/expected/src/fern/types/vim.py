

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vim_config import VimConfig


class Vim(UniversalBaseModel):
    """
    A new VIM
    """

    id: str = pydantic.Field()
    """
    Unique id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the new VIM
    """

    auth_url: str = pydantic.Field()
    """
    VIM's authentication URL - example: http://10.200.64.2:5000/v3/
    """

    username: str = pydantic.Field()
    """
    The admin username
    """

    password: str = pydantic.Field()
    """
    The admin password
    """

    admin_project_name: str = pydantic.Field()
    """
    The admin project
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    VIM's location
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    VIM's type
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the VIM's OS
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the VIM
    """

    infrastructure_monitoring: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional - The URL of the Prometheus system that is responsible for monitoring the VIM
    """

    config: typing.Optional[VimConfig] = pydantic.Field(default=None)
    """
    Optional parameters regarding the VIM operation - example: Security group
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
