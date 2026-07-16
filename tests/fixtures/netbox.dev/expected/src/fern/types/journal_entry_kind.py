

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .journal_entry_kind_label import JournalEntryKindLabel
from .journal_entry_kind_value import JournalEntryKindValue


class JournalEntryKind(UniversalBaseModel):
    label: JournalEntryKindLabel
    value: JournalEntryKindValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
