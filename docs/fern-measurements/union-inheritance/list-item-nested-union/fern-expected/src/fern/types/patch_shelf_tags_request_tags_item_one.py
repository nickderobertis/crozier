

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_shelf_tags_request_tags_item_one_operation import PatchShelfTagsRequestTagsItemOneOperation


class PatchShelfTagsRequestTagsItemOne(UniversalBaseModel):
    label: str
    operation: PatchShelfTagsRequestTagsItemOneOperation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
