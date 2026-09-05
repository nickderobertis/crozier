

from __future__ import annotations

import typing

from .batch_entry_query import BatchEntryQuery

if typing.TYPE_CHECKING:
    from .batch_entry_for_each import BatchEntryForEach
BatchEntry = typing.Union[BatchEntryQuery, "BatchEntryForEach"]
