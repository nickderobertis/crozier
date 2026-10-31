

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_service_command import UserServiceCommand


class CallbacksMapping(UniversalBaseModel):
    metrics: typing.Optional[UserServiceCommand] = pydantic.Field(default=None)
    """
    command to recover prometheus metrics from a specific user service
    """

    before_shutdown: typing.Optional[typing.List[UserServiceCommand]] = pydantic.Field(default=None)
    """
    commands to run before shutting down the user servicescommands get executed first to last, multiple commands for the sameuser services are allowed
    """

    inactivity: typing.Optional[UserServiceCommand] = pydantic.Field(default=None)
    """
    command used to figure out for how much time the user service(s) were inactive for
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
