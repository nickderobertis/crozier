

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_quote_by_id_quote_response_data_links_item_type import GetQuoteByIdQuoteResponseDataLinksItemType


class GetQuoteByIdQuoteResponseDataLinksItem(UniversalBaseModel):
    href: str
    rel: str
    type: GetQuoteByIdQuoteResponseDataLinksItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
