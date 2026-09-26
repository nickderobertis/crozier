

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_quote_response_data_links_item_type import AddQuoteResponseDataLinksItemType


class AddQuoteResponseDataLinksItem(UniversalBaseModel):
    href: str
    rel: str
    type: AddQuoteResponseDataLinksItemType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
