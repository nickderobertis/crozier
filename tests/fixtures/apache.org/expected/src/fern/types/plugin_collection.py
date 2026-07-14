

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .plugin_collection_item import PluginCollectionItem


class PluginCollection(CollectionInfo):
    """
    A collection of plugin.

    *New in version 2.1.0*
    """

    plugins: typing.Optional[typing.List[PluginCollectionItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
