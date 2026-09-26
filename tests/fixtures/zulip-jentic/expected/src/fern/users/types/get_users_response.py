

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.user import User


class GetUsersResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    members: typing.Optional[typing.List[User]] = pydantic.Field(default=None)
    """
    A list of `user` objects, each containing details about a user in the
    organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
