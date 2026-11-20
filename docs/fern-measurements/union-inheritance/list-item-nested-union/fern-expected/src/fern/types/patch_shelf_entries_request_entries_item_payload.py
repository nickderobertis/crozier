

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_shelf_entries_request_entries_item_payload_operation import (
    PatchShelfEntriesRequestEntriesItemPayloadOperation,
)
from .patch_shelf_entries_request_entries_item_payload_payload import PatchShelfEntriesRequestEntriesItemPayloadPayload


class PatchShelfEntriesRequestEntriesItemPayload(UniversalBaseModel):
    label: str
    operation: PatchShelfEntriesRequestEntriesItemPayloadOperation
    payload: PatchShelfEntriesRequestEntriesItemPayloadPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
