

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResolvedIdentifier(UniversalBaseModel):
    """
    A successfully resolved identifier.
    """

    id: str = pydantic.Field()
    """
    The internal user ID of the resolved user.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the user on the remote network.
    """

    avatar_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The avatar of the user on the remote network.
    """

    identifiers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of identifiers for the user on the remote network.
    """

    mxid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Matrix user ID of the ghost representing the user.
    """

    dm_room_mxid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Matrix room ID of the direct chat with the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
