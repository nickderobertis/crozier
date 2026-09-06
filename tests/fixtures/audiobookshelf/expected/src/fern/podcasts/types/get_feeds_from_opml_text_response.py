

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_feeds_from_opml_text_response_feeds_item import GetFeedsFromOpmlTextResponseFeedsItem


class GetFeedsFromOpmlTextResponse(UniversalBaseModel):
    feeds: typing.Optional[typing.List[GetFeedsFromOpmlTextResponseFeedsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
