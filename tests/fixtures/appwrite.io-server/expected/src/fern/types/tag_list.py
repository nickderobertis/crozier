

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tag import Tag


class TagList(UniversalBaseModel):
    """
    Tags List
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    tags: typing.List[Tag] = pydantic.Field()
    """
    List of tags.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
