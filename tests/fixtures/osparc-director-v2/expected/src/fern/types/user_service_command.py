

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_service_command_command import UserServiceCommandCommand


class UserServiceCommand(UniversalBaseModel):
    service: str = pydantic.Field()
    """
    name of the docker-compose service in the docker-compose spec
    """

    command: UserServiceCommandCommand = pydantic.Field()
    """
    command to run in container
    """

    timeout: float = pydantic.Field()
    """
    after this interval the command will be timed-out
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
