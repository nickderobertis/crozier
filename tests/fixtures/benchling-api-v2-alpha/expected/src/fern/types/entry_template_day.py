

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_template_day_notes_item import EntryTemplateDayNotesItem


class EntryTemplateDay(UniversalBaseModel):
    day: typing.Optional[int] = pydantic.Field(default=None)
    """
    1 indexed day signifier. If 0 is returned, that means the EntryTemplateDay is a section with a title but no specified Day.
    """

    notes: typing.Optional[typing.List[EntryTemplateDayNotesItem]] = None
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
