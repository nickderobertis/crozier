

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .connection_collection_item import ConnectionCollectionItem


class Connection(ConnectionCollectionItem):
    """
    Full representation of the connection.
    """

    extra: typing.Optional[str] = pydantic.Field(default=None)
    """
    Other values that cannot be put into another field, e.g. RSA keys.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password of the connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
