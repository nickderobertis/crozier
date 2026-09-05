

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_id_int import GroupIdInt


class GroupGetBase(UniversalBaseModel):
    gid: GroupIdInt = pydantic.Field()
    """
    the group's unique ID
    """

    label: str = pydantic.Field()
    """
    the group's display name
    """

    description: str
    thumbnail: typing.Optional[str] = pydantic.Field(default=None)
    """
    a link to the group's thumbnail
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
