

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_user_filters import BaseUserFilters
from .recovery_code import RecoveryCode
from .user_totp_config import UserTotpConfig


class UserFilters(BaseUserFilters):
    require_password_change: typing.Optional[bool] = pydantic.Field(default=None)
    """
    User must change password from WebClient/REST API at next login
    """

    totp_config: typing.Optional[UserTotpConfig] = None
    recovery_codes: typing.Optional[typing.List[RecoveryCode]] = None
    tls_certs: typing.Optional[typing.List[str]] = None
    additional_emails: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
