

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .connection_collection_item import ConnectionCollectionItem


class ConnectionCollection(CollectionInfo):
    """
    Collection of connections.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    connections: typing.Optional[typing.List[ConnectionCollectionItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
