

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_table_cell import EntryTableCell


class EntryTableRow(UniversalBaseModel):
    """
    Each has property 'cells' that is an array of cell objects
    """

    cells: typing.Optional[typing.List[EntryTableCell]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
