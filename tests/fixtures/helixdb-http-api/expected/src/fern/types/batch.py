

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Batch(UniversalBaseModel):
    entries: typing.List["BatchEntry"]
    returns: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .batch_entry import BatchEntry
from .batch_entry_for_each import BatchEntryForEach
from .batch_entry_for_each_for_each import BatchEntryForEachForEach

update_forward_refs(
    Batch, BatchEntry=BatchEntry, BatchEntryForEach=BatchEntryForEach, BatchEntryForEachForEach=BatchEntryForEachForEach
)
