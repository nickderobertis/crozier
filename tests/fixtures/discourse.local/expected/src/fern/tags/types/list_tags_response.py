

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_tags_response_extras import ListTagsResponseExtras
from .list_tags_response_tags_item import ListTagsResponseTagsItem


class ListTagsResponse(UniversalBaseModel):
    extras: typing.Optional[ListTagsResponseExtras] = None
    tags: typing.Optional[typing.List[ListTagsResponseTagsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
