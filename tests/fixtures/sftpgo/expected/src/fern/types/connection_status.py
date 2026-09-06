

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_status_protocol import ConnectionStatusProtocol
from .transfer import Transfer


class ConnectionStatus(UniversalBaseModel):
    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    connected username
    """

    connection_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    unique connection identifier
    """

    client_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    client version
    """

    remote_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remote address for the connected client
    """

    connection_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    connection time as unix timestamp in milliseconds
    """

    command: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last SSH/FTP command or WebDAV method
    """

    last_activity: typing.Optional[int] = pydantic.Field(default=None)
    """
    last client activity as unix timestamp in milliseconds
    """

    protocol: typing.Optional[ConnectionStatusProtocol] = None
    active_transfers: typing.Optional[typing.List[Transfer]] = None
    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    Node identifier, omitted for single node installations
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
