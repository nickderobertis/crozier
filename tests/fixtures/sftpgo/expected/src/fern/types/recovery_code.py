

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret import Secret


class RecoveryCode(UniversalBaseModel):
    """
    Recovery codes to use if the user loses access to their second factor auth device. Each code can only be used once, you should use these codes to login and disable or reset 2FA for your account
    """

    secret: typing.Optional[Secret] = None
    used: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
