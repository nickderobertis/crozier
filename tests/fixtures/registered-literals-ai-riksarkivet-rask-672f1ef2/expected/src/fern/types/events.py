

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_record import EventRecord


class Events(UniversalBaseModel):
    """
    The most-recent ingested OpenLineage events (newest first).

    ``next_cursor`` (additive, 2026-07-11): pass back as ``?after=`` to page OLDER events (keyset
    over ``seq``). ``None`` = the feed is exhausted.
    """

    events: typing.List[EventRecord]
    next_cursor: typing.Optional[int] = None
    oldest_seq: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
