

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectionsResponseItemLastHandshake(UniversalBaseModel):
    """
    Structure holding detailed information about the connection
    """

    agent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Agent name
    """

    chain_id: typing.Optional[str] = None
    generation: typing.Optional[int] = pydantic.Field(default=None)
    """
    Generation number
    """

    head_id: typing.Optional[str] = None
    head_num: typing.Optional[int] = pydantic.Field(default=None)
    """
    Head number
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base58 encoded EOSIO public key
    """

    last_irreversible_block_id: typing.Optional[str] = None
    last_irreversible_block_num: typing.Optional[int] = pydantic.Field(default=None)
    """
    Last irreversible block number
    """

    network_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Incremental value above a computed base
    """

    node_id: typing.Optional[str] = None
    os: typing.Optional[str] = pydantic.Field(default=None)
    """
    Operating system name
    """

    p2p_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    IP address or URL of the peer
    """

    sig: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base58 encoded EOSIO cryptographic signature
    """

    time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date/time string in the format YYYY-MM-DDTHH:MM:SS.sss
    """

    token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
