

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_intelligences_response_items_item import ListIntelligencesResponseItemsItem


class ListIntelligencesResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    page: typing.Optional[int] = None
    num_pages: typing.Optional[int] = None
    page_size: typing.Optional[int] = None
    total_count: typing.Optional[int] = None
    items: typing.Optional[typing.List[ListIntelligencesResponseItemsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
