

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .portal_sources_item_tables_item import PortalSourcesItemTablesItem


class PortalSourcesItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    tables: typing.Optional[typing.List[PortalSourcesItemTablesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
