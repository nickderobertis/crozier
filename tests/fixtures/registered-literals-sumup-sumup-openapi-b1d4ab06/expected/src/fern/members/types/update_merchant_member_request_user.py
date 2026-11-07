

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateMerchantMemberRequestUser(UniversalBaseModel):
    """
    Allows you to update user data of managed users.
    """

    nickname: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's nickname. Used for display purposes only.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password of the member to add. Only used if `is_managed_user` is true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
