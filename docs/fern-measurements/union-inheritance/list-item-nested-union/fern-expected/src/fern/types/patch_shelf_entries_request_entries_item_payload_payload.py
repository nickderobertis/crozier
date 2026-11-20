

import typing

from .patch_shelf_entries_request_entries_item_payload_payload_one_item import (
    PatchShelfEntriesRequestEntriesItemPayloadPayloadOneItem,
)
from .patch_shelf_entries_request_entries_item_payload_payload_zero import (
    PatchShelfEntriesRequestEntriesItemPayloadPayloadZero,
)

PatchShelfEntriesRequestEntriesItemPayloadPayload = typing.Union[
    typing.Optional[PatchShelfEntriesRequestEntriesItemPayloadPayloadZero],
    typing.List[typing.Optional[PatchShelfEntriesRequestEntriesItemPayloadPayloadOneItem]],
]
