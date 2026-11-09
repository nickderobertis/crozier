

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bridge_state import BridgeState
from .remote_profile import RemoteProfile
from .user_login_id import UserLoginId


class WhoamiLogin(UniversalBaseModel):
    """
    The info of an individual login
    """

    state: BridgeState
    id: UserLoginId
    name: str = pydantic.Field()
    """
    A human-readable name for the login. Defined by the network connector.
    """

    profile: RemoteProfile
    space_room: typing.Optional[str] = pydantic.Field(default=None)
    """
    The personal filtering space room ID for this login.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
