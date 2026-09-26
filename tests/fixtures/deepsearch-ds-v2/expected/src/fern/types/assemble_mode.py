

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assemble_mode_page_elements_item import AssembleModePageElementsItem
from .assemble_mode_tables_item import AssembleModeTablesItem


class AssembleMode(UniversalBaseModel):
    page_elements: typing.List[AssembleModePageElementsItem]
    tables: typing.List[AssembleModeTablesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
