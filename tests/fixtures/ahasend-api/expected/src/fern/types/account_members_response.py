

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_members_response_object import AccountMembersResponseObject
from .user_account import UserAccount


class AccountMembersResponse(UniversalBaseModel):
    object: AccountMembersResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[UserAccount] = pydantic.Field()
    """
    Array of account members
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
