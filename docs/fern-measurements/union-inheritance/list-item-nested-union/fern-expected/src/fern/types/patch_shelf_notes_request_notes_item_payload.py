

import typing

from .patch_shelf_notes_request_notes_item_payload_one_item import PatchShelfNotesRequestNotesItemPayloadOneItem
from .patch_shelf_notes_request_notes_item_payload_zero import PatchShelfNotesRequestNotesItemPayloadZero

PatchShelfNotesRequestNotesItemPayload = typing.Union[
    typing.Optional[PatchShelfNotesRequestNotesItemPayloadZero],
    typing.List[typing.Optional[PatchShelfNotesRequestNotesItemPayloadOneItem]],
]
