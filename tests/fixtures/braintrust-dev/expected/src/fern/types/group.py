

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Group(UniversalBaseModel):
    """
    A group is a collection of users which can be assigned an ACL

    Groups can consist of individual users, as well as a set of groups they inherit from
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the group
    """

    org_id: str = pydantic.Field()
    """
    Unique id for the organization that the group belongs under
    
    It is forbidden to change the org after creating a group
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the group
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of group creation
    """

    name: str = pydantic.Field()
    """
    Name of the group
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the group
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of group deletion, or null if the group is still active
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
