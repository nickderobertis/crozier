

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_user_to_account_request_users_item_identification import AddUserToAccountRequestUsersItemIdentification


class AddUserToAccountRequestUsersItem(UniversalBaseModel):
    identification: AddUserToAccountRequestUsersItemIdentification = pydantic.Field()
    """
    User identification requires a userId, email or both
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
