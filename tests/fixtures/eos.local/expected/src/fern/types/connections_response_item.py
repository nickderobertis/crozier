

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connections_response_item_last_handshake import ConnectionsResponseItemLastHandshake


class ConnectionsResponseItem(UniversalBaseModel):
    connecting: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the peer is connecting, otherwise false
    """

    last_handshake: typing.Optional[ConnectionsResponseItemLastHandshake] = pydantic.Field(default=None)
    """
    Structure holding detailed information about the connection
    """

    peer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address or URL of the peer
    """

    syncing: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the peer is syncing, otherwise false
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
