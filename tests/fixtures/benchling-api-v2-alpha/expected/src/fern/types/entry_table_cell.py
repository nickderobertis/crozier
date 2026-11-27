

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_link import EntryLink


class EntryTableCell(UniversalBaseModel):
    link: typing.Optional[EntryLink] = pydantic.Field(default=None)
    """
    A Link Resource if this cell contained a hyperlink. Otherwise, link will be omitted from the cell object. (Note: inventory and user types are not yet supported.)
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The textual content of the cell. If the cell was originally a formula, this will be the evaluated version of the formula.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
