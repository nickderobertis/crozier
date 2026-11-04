

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes import Attributes
from .invite import Invite
from .membership_status import MembershipStatus
from .membership_user import MembershipUser
from .metadata import Metadata


class Member(UniversalBaseModel):
    """
    A member is user within specific resource identified by resource id, resource type, and associated roles.
    """

    id: str = pydantic.Field()
    """
    ID of the member.
    """

    roles: typing.List[str] = pydantic.Field()
    """
    User's roles.
    """

    permissions: typing.List[str] = pydantic.Field()
    """
    User's permissions.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the member was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the member was last updated.
    """

    user: typing.Optional[MembershipUser] = None
    invite: typing.Optional[Invite] = None
    status: MembershipStatus
    metadata: typing.Optional[Metadata] = None
    attributes: typing.Optional[Attributes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
