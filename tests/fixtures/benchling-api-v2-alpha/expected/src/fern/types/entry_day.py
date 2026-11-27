

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_note_part import EntryNotePart


class EntryDay(UniversalBaseModel):
    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Date string
    """

    notes: typing.Optional[typing.List[EntryNotePart]] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional title of a section if sections are enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
