

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_shelf_notes_request_notes_item_payload import PatchShelfNotesRequestNotesItemPayload


class PatchShelfNotesRequestNotesItem(UniversalBaseModel):
    label: str
    payload: PatchShelfNotesRequestNotesItemPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
