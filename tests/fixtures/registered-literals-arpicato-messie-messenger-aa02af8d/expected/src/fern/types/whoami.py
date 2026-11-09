

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bridge_name import BridgeName
from .login_flow import LoginFlow
from .whoami_login import WhoamiLogin


class Whoami(UniversalBaseModel):
    """
    Info about the bridge and user
    """

    network: BridgeName
    login_flows: typing.List[LoginFlow] = pydantic.Field()
    """
    The login flows that the bridge supports.
    """

    homeserver: str = pydantic.Field()
    """
    The server name the bridge is running on.
    """

    bridge_bot: str = pydantic.Field()
    """
    The Matrix user ID of the bridge bot.
    """

    command_prefix: str = pydantic.Field()
    """
    The command prefix used by this bridge.
    """

    management_room: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Matrix management room ID of the user who made the /whoami call.
    """

    logins: typing.List[WhoamiLogin] = pydantic.Field()
    """
    The logins of the user who made the /whoami call
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
