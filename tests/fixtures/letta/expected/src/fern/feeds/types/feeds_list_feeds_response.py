

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feeds_list_feeds_response_feeds_item import FeedsListFeedsResponseFeedsItem


class FeedsListFeedsResponse(UniversalBaseModel):
    feeds: typing.List[FeedsListFeedsResponseFeedsItem]
    has_next_page: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
