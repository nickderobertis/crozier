

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .membership_role import MembershipRole
from .membership_user import MembershipUser


class Membership(UniversalBaseModel):
    """
    A Membership
    """

    id: str = pydantic.Field()
    """
    The id of the membership
    """

    role: typing.Optional[MembershipRole] = pydantic.Field(default=None)
    """
    The role of the member
    """

    user: MembershipUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
