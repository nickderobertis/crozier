

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .me_response_account import MeResponseAccount
from .me_user import MeUser


class MeResponse(UniversalBaseModel):
    account: MeResponseAccount = pydantic.Field()
    """
    Account state for the current user
    """

    user: MeUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
