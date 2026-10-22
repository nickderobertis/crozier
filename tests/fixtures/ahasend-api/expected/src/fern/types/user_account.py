

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_account_role import UserAccountRole


class UserAccount(UniversalBaseModel):
    created_at: dt.datetime = pydantic.Field()
    """
    When the relationship was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the relationship was last updated
    """

    user_id: str = pydantic.Field()
    """
    User ID
    """

    account_id: str = pydantic.Field()
    """
    Account ID
    """

    role: UserAccountRole = pydantic.Field()
    """
    User role in the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
