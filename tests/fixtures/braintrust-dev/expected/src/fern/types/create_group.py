

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateGroup(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the group
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the group
    """

    member_users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of users which belong to this group
    """

    member_groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Ids of the groups this group inherits from
    
    An inheriting group has all the users contained in its member groups, as well as all of their inherited users
    """

    org_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For nearly all users, this parameter should be unnecessary. But in the rare case that your API key belongs to multiple organizations, you may specify the name of the organization the group belongs in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
