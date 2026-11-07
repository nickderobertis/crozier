

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes import Attributes
from .invite import Invite
from .membership_resource import MembershipResource
from .membership_status import MembershipStatus
from .metadata import Metadata
from .resource_type import ResourceType


class Membership(UniversalBaseModel):
    """
    A membership associates a user with a resource, memberships is defined by user, resource, resource type, and associated roles.
    """

    id: str = pydantic.Field()
    """
    ID of the membership.
    """

    resource_id: str = pydantic.Field()
    """
    ID of the resource the membership is in.
    """

    type: ResourceType
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
    The timestamp of when the membership was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp of when the membership was last updated.
    """

    invite: typing.Optional[Invite] = None
    status: MembershipStatus
    metadata: typing.Optional[Metadata] = None
    attributes: typing.Optional[Attributes] = None
    resource: MembershipResource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
