

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dev_list_users_response_direct_admins_item import DevListUsersResponseDirectAdminsItem
from .dev_list_users_response_direct_users_item import DevListUsersResponseDirectUsersItem


class DevListUsersResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    direct_admins: typing.Optional[typing.List[DevListUsersResponseDirectAdminsItem]] = pydantic.Field(default=None)
    """
    A list of administrators in the development server.
    """

    direct_users: typing.Optional[typing.List[DevListUsersResponseDirectUsersItem]] = pydantic.Field(default=None)
    """
    A list of non-admin users in the development server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
