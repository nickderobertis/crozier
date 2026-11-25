

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .portal_sources_item_tables_item_configuration import PortalSourcesItemTablesItemConfiguration
from .seamless_link import SeamlessLink


class PortalSourcesItemTablesItem(UniversalBaseModel):
    configuration: typing.Optional[PortalSourcesItemTablesItemConfiguration] = None
    links: typing.Optional[typing.List[SeamlessLink]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
