

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .users_get_response_data_users_item import UsersGetResponseDataUsersItem


class UsersGetResponseData(UniversalBaseModel):
    users: typing.List[UsersGetResponseDataUsersItem] = pydantic.Field()
    """
    List of users
    """

    total: float = pydantic.Field()
    """
    Total number of users
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
