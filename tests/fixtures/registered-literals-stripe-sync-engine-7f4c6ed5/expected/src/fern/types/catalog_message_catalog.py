

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_message_catalog_streams_item import CatalogMessageCatalogStreamsItem


class CatalogMessageCatalog(UniversalBaseModel):
    """
    Catalog of available streams.
    """

    streams: typing.List[CatalogMessageCatalogStreamsItem] = pydantic.Field()
    """
    All streams available from this source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
