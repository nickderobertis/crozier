

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_dto import ItemDto


class JsonFeedDto(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provides more detail on what the feed is about
    """

    home_page_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the resource that the feed describes
    """

    items: typing.List[ItemDto]
    title: str = pydantic.Field()
    """
    Name of the feed
    """

    version: str = pydantic.Field()
    """
    URL of the version of the format the feed uses
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
