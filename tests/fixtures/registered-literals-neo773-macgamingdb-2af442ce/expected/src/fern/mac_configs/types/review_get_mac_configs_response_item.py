

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .review_get_mac_configs_response_item_metadata import ReviewGetMacConfigsResponseItemMetadata


class ReviewGetMacConfigsResponseItem(UniversalBaseModel):
    id: str
    identifier: str
    label: str
    metadata: ReviewGetMacConfigsResponseItemMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
