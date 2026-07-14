

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .searched_group import SearchedGroup


class GroupSearchResults(UniversalBaseModel):
    """
    Describes the response received when searching for groups.
    """

    count: int = pydantic.Field()
    """
    The total number of groups that matched the query that produced the result set (may be 
    more than the number of groups in the result set).
    """

    groups: typing.List[SearchedGroup] = pydantic.Field()
    """
    The groups returned in the result set.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
