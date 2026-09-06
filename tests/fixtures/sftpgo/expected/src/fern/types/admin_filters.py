

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_preferences import AdminPreferences
from .admin_totp_config import AdminTotpConfig
from .recovery_code import RecoveryCode


class AdminFilters(UniversalBaseModel):
    allow_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    only clients connecting from these IP/Mask are allowed. IP/Mask must be in CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32"
    """

    allow_api_key_auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    API key auth allows to impersonate this administrator with an API key
    """

    require_two_factor: typing.Optional[bool] = None
    require_password_change: typing.Optional[bool] = None
    totp_config: typing.Optional[AdminTotpConfig] = None
    recovery_codes: typing.Optional[typing.List[RecoveryCode]] = None
    preferences: typing.Optional[AdminPreferences] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
