

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .table_former_mode import TableFormerMode


class TableStructureOptions(UniversalBaseModel):
    do_table_structure: typing.Optional[bool] = None
    table_structure_mode: typing.Optional[TableFormerMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
