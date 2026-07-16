

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_journal_entry_kind import WritableJournalEntryKind


class WritableJournalEntry(UniversalBaseModel):
    assigned_object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    assigned_object_id: int
    assigned_object_type: str
    comments: str
    created: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[int] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    kind: typing.Optional[WritableJournalEntryKind] = None
    last_updated: typing.Optional[dt.datetime] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
