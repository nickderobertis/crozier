

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_shelf_tags_request_tags_item_payload_operation import PatchShelfTagsRequestTagsItemPayloadOperation
from .patch_shelf_tags_request_tags_item_payload_payload import PatchShelfTagsRequestTagsItemPayloadPayload


class PatchShelfTagsRequestTagsItemPayload(UniversalBaseModel):
    label: str
    operation: PatchShelfTagsRequestTagsItemPayloadOperation
    payload: typing.Optional[PatchShelfTagsRequestTagsItemPayloadPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
