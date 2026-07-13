

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_content_item_public_contract import ContentContentItemPublicContract


class TrendingTrendingEntrySupportArticle(UniversalBaseModel):
    article: typing.Optional[ContentContentItemPublicContract] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
